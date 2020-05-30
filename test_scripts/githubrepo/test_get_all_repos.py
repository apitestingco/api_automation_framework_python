from src.helpers.utils import get_data, get_auth
from src.helpers import verify_common
from src.constants.data import get_repos_url
from src.models.contracts import get_all_repo_contract

'''
Author : Pramod
Objective :  Get First Repo for the User
1. Verify the import Keys
2. Verify the Headers, Status code and Id Exist.
3. JSON Schema Validation.
'''


class TestFunctional(object):

    def test_verify_get_all_response(self):
        data = get_data(get_repos_url(username=get_auth()[0]), auth=get_auth(), in_json=True)
        verify_common.verify_repo_data(data, 'Demo11236')

    def test_verify_get_all_http_code(self):
        data = get_data(get_repos_url(username=get_auth()[0]), auth=get_auth(), in_json=False)
        verify_common.verify_http_code(data, '200')

    def test_verify_get_all_important_keys(self):
        data = get_data(get_repos_url(username=get_auth()[0]), auth=get_auth(), in_json=True)
        verify_common.verify_important_keys(data, 'id,,name,html_url')

    def test_verify_get_all_headers(self):
        data = get_data(get_repos_url(username=get_auth()[0]), auth=get_auth(), in_json=False)
        verify_common.verify_headers(data, 'application/json; charset=utf-8')

    def test_verify_get_all_id_exist(self):
        data = get_data(get_repos_url(username=get_auth()[0]), auth=get_auth(), in_json=True)
        verify_common.verify_id_exist(data, 'id')


class TestContract(object):
    def test_contract_get_all(self):
        data = get_data(get_repos_url(username=get_auth()[0]), auth=get_auth(), in_json=True)
        verify_common.verify_contract(data, get_all_repo_contract.get_all_repos)
