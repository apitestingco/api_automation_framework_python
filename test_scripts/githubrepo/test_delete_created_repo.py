from src.constants.data import post_repo_url, delete_repo_url, get_single_repo_url
from src.helpers import verify_common
from src.helpers.utils import get_auth, post_data, delete_data
from src.helpers.utils import get_data

'''
Author : Pramod
Objective :  Create and Delete a Repo and Verify by Get Call
'''


class TestFunctional(object):

    def test_verify_delete_repo(self):
        # For delete we have to create a repo first
        repo_create = post_data(post_repo_url(), auth=get_auth(), payload=None ,in_json= False)
        repo_deleted_data = delete_data(delete_repo_url(username=get_auth()[0], repo_name=repo_create.json()["name"]),
                                        auth=get_auth(), in_json=False)
        verify_common.verify_delete_http_status(repo_deleted_data, 204)

        # Get that repo and verify
        data = get_data(get_single_repo_url(username=get_auth()[0], repo_name=repo_create.json()["name"]),
                        auth=get_auth(), in_json=False)
        verify_common.verify_get_single_repo(data, 404)
