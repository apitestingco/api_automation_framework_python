import json
import requests


def get_auth():
    f = open("src/helpers/creds.json")
    creds = json.load(f)
    username = str(creds["username"])
    password = str(creds["password"])
    auth = (username, password)
    f.close()
    return auth


def get_data(url, auth, in_json):
    data = requests.get(url=url, auth=auth)
    if in_json is True:
        return data.json()
    return data


def post_data(url, auth, payload, in_json):
    if payload is None:
        payload = {
            "name": "TempRepo",
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        }
    post_response_data = requests.post(url, auth=(auth), data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def patch_data(url, auth, payload, in_json):
    patch_response_data = requests.patch(url, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_data(url, auth, in_json):
    delete_response_data = requests.delete(url, auth=(auth))
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
