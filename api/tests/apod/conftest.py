from urllib.parse import urljoin

import pytest


@pytest.fixture
def apod_api_mock(client, requests_mock) -> None:
    apod_url_path = "/api/apod/"
    apod_api_url = urljoin(client.base_url, apod_url_path)
    return_data = {
        "copyright": "Gianni Sarcone",
        "date": "2021-10-16",
        "explanation": "Only natural colors of the Moon in planet Earth's sky appear in this creative visual presentation. Arranged as pixels in a framed image, the lunar disks were photographed at different times. Their varying hues are ultimately due to reflected sunlight affected by changing atmospheric conditions and the alignment geometry of Moon, Earth, and Sun. Here, the darkest lunar disks are the colors of earthshine. A description of earthshine, in terms of sunlight reflected by Earth's oceans illuminating the Moon's dark surface, was written over 500 years ago by Leonardo da Vinci.  But stand farther back from your monitor or just shift your gaze to the smaller versions of the image. You might also see one of da Vinci's most famous works of art.  Tonight: International Observe the Moon Night",
        "hdurl": "https://apod.nasa.gov/apod/image/2110/Moonalisa_base_corr.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": "The Moona Lisa",
        "url": "https://apod.nasa.gov/apod/image/2110/Moonalisa_Example1024.jpg",
    }
    requests_mock.register_uri("GET", apod_api_url, json=return_data)
