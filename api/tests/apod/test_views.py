from starlette import status


def test_get_apod(client, apod_api_mock):
    endpoint_url_path = "/api/apod/"
    response = client.get(endpoint_url_path)

    result_dict = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result_dict["title"] == "The Moona Lisa"
    assert result_dict["date"] == "2021-10-16"
