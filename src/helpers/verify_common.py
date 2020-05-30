from jsonschema import validate


def verify_repo_data(data, expected_data):
    for i in data:
        print(i)
        if i['name'] == "Demo11236":
            assert i['name'] == expected_data, "Expected Repo Name is : " + expected_data


def verify_single_repo_data(data, expected_data):
    assert data['name'] == expected_data, "Expected Repo Name is : " + expected_data


def verify_http_code(data, expected_data):
    assert data.status_code == int(expected_data), "Expected HTTP is : " + expected_data


def verify_important_keys(data, expected_data):
    assert data[0]['name'] == expected_data, "Expected Repo Name is : " + expected_data


def verify_important_keys(data, expected_data):
    assert len(str(data[0]['id'])) != 0, "Id Exist in the Reponse"
    assert len(data[0]['name']) != 0, "Name in the Reponse"
    assert len(data[0]['html_url']) != 0, "Html Url Exist in the Reponse"


def verify_headers(data, expected_data):
    assert data.headers["Content-Type"] == expected_data, "Content-Type is : " + expected_data


def verify_id_exist(data, expected_data):
    assert len(str(data[0]["id"])) != 0, "Id Exist  : "


def verify_delete_http_status(data, expected_data):
    assert data.status_code == expected_data


def verify_get_single_repo(data, expected_data):
    assert data.status_code == expected_data


def verify_contract(data, expected_schema):
    validate(instance=data, schema=expected_schema)
