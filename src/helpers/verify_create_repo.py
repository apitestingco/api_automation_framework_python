def verify_repo_data(data, expected_data):
    assert len(str(data['id'])) != 0, "Id Exist in the Response"
    assert len(data['name']) != 0, "Name in the Response"
    assert len(data['html_url']) != 0, "Html Url Exist in the Response"
    assert data['name'] == expected_data, "Expected Repo Name is : " + expected_data


