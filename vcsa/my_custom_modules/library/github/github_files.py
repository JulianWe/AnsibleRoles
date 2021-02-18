

from builtins import object

from ansible.module_utils.basic import AnsibleModule
from github import Github, ContentFile
from github.GithubException import UnknownObjectException, BadCredentialsException

import urllib3

urllib3.disable_warnings()

DOCUMENTATION = r'''
---
module: github_files
short_description: GitHub file handling
description: The module can be used to read, modify or create files in a GitHub repository.
authors: "Marc Wappler (marc.wappler@sap.com)"
version_added: "2.6"
options:
    action:
        description: action to perform on repo
        possible_values: ['change_file', 'delete_file', 'get_file']
        required: True
    github_server:
        description: github server to connect to
        required: True
    user:
        description: github user for auth
        required: True
    token:
        description: github token for auth
        required: True
    repo:
        description: github repo to change
        required: True
    file_path:
        description: target file to be modified
        required: True
    file_content:
        description: contains the content in case of file modifications
    commit_message:
        description: commit message for file modifications
'''

EXAMPLES = r'''
- hosts: localhost
  gather_facts: false
  tasks:
    - name: read and commit ansible.cfg
      github_files:
        action: change_file
        commit_message: write ansible.cfg to repo
        repo: Infrastructure-Automation/cc-vmware-security
        file_path: tracking/ansible.cfg
        file_content: "{{ lookup('file', '/ccloud/ansible/ansible.cfg') }}"
        github_server: github.wdf.sap.corp
        token: "{{ github_token }}"
        user: "{{ github_user }}"
'''

RETURN = r'''
file_content:
    description: base64 encoded file content
    returned: when action = 'get_file'
    type: str
encoding:
    description: file content encoding
    returned: when action = 'get_file'
    type: str
commit_sha:
    description: git commit hash value
    returned: when action = 'change_file' or 'delete_file'
    type: str
'''


class GitHubFiles(object):
    def __init__(self, ansible_module_specs, requirements):
        self.module = AnsibleModule(argument_spec=ansible_module_specs,
                                    supports_check_mode=False,
                                    required_if=requirements)

        self.server_string = "https://{0}/api/v3".format(
            self.module.params['github_server'])
        try:
            self.github_api = Github(base_url=self.server_string,
                                     login_or_token=self.module.params['token'],
                                     verify=False)

            self.github_repo = self.github_api.get_repo(
                self.module.params['repo'])

        except UnknownObjectException as error:
            self.module.fail_json(
                msg="Provided repo not found in GitHub. Message: {0}".format(error))

        except BadCredentialsException as error:
            self.module.fail_json(
                msg="Authorization to GitHub failed. Message: {0}".format(error))

    def set_fileinfo(self):
        """
        Get and set file info from file in GitHub repo.
        """

        try:
            self.args['target_file'] = self.github_repo.get_contents(
                self.module.params['file_path'])

        except UnknownObjectException:
            self.args['target_file'] = None

    def get_file(self):
        """
        Return content from file in GitHub repo.
        """

        data = dict(file_content=self.args['target_file'].content,
                    encoding=self.args['target_file'].encoding)

        ret = dict(msg="File object received successfully.",
                   changed=False, **data)

        return ret

    def change_file(self):
        """
        Update/create file in repo.
        """

        if isinstance(self.args['target_file'], ContentFile.ContentFile):
            data = self.github_repo.update_file(
                self.args['target_file'].path,
                self.args['commit'],
                self.args['file_content'],
                self.args['target_file'].sha
            )
        else:
            data = self.github_repo.create_file(
                self.args['file_path'],
                self.args['commit'],
                self.args['file_content']
            )

        ret = dict(msg="File updated/created in repo.",
                   commit_sha=data['commit'].sha, changed=True)

        return ret

    def delete_file(self):
        """
        Delete a file in repo.
        """
        data = self.github_repo.delete_file(self.args['target_file'].path,
                                            self.args['commit'],
                                            self.args['target_file'].sha
                                            )

        ret = dict(msg="File successfully deleted.",
                   commit_sha=data['commit'].sha, changed=True)

        return ret

    def checkout_params(self):
        """
        Collect and prepare parameters for API calls.
        Do some basic checks.
        """

        self.args = dict(commit=self.module.params.get('commit_message'),
                         file_path=self.module.params.get('file_path'),
                         action=self.module.params['action'],
                         file_content=self.module.params.get('file_content'))

        self.set_fileinfo()

        # fail if pre-existent file is required
        if self.args['action'] == "delete_file" or self.args['action'] == "get_file":
            if not isinstance(self.args['target_file'], ContentFile.ContentFile):
                self.module.fail_json(
                    msg="Target file not found in GitHub repo.")

    def call_api_method(self):
        """
        Run GitHub repo action.
        """

        self.checkout_params()
        if self.args['action'] in dir(self):
            self.module.exit_json(**getattr(self, self.args['action'])())

        else:
            self.module.fail_json(
                msg="GitHub action unknown: {0}".format(self.args['action']))


def main():
    module_specs = dict(
        action=dict(type="str",
                    required=True,
                    choices=['change_file', 'delete_file', 'get_file']),
        token=dict(type="str", required=True, no_log=True),
        user=dict(type="str", required=True, no_log=True),
        file_path=dict(type="str", required=True),
        commit_message=dict(type="str", required=False),
        file_content=dict(type="str", required=False),
        github_server=dict(type="str", required=True),
        repo=dict(type="str", required=True)
    )

    sticky_params = [['action', 'change_file', ['commit_message', 'file_content']],
                     ['action', 'delete_file', ['commit_message']]]

    init = GitHubFiles(module_specs, sticky_params)
    init.call_api_method()


if __name__ == "__main__":
    main()
