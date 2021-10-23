from starlette import status


def test_apod_view(client):
    apod_view_url = "/apod"
    response = client.get(apod_view_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.context["date"] == "2021-10-16"
    assert response.context["title"] == "The Moona Lisa"
