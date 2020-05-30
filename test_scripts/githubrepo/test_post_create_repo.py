import random

from src.constants.data import post_repo_url, delete_repo_url, get_single_repo_url
from src.helpers import verify_common, verify_create_repo
from src.helpers.utils import get_auth, post_data, delete_data
from src.helpers.utils import get_data

'''
Author : Pramod
Objective :  Create and Verify by Get Call
'''


class TestFunctional(object):

    def test_setup(self):
        print("#1")
        global data
        global name
        name = "TempRepo" + str(random.randint(1, 999))
        payload = {"name": name, "description": "This is your first repository",
                   "homepage": "https://github.com", "private": False, "has_issues": True, "has_projects": True,
                   "has_wiki": True}
        data = post_data(post_repo_url(), auth=get_auth(), payload=payload, in_json=False)

    def test_verify_created_repo(self):
        verify_create_repo.verify_repo_data(data.json(), name)

    def test_verify_repo_by_get(self):
        data = get_data(get_single_repo_url(username=get_auth()[0], repo_name=name),
                        auth=get_auth(), in_json=True)
        verify_common.verify_single_repo_data(data, name)

    def teardown_module(module):
        print("End")

