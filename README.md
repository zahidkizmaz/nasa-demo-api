# <center> Nasa Api - Astronomy Picture of the Day </center>

<p align="center">
  <img src="https://apod.nasa.gov/apod/image/2110/Moonalisa_base_corr.jpg" width="350" title="The Moona Lisa">
</p>

[![Python 3.10](https://img.shields.io/badge/python-3.10-d.svg)](https://www.python.org/downloads/release/python-3100/)
<hr/>
This is a simple async Fast Api application that uses Nasa Api. This projects aims to discover Fast Api and it is features.

## Running on local
1. Clone the repo.
2. Make sure you have [poetry](https://python-poetry.org/docs/#installation) installed.
3. Set this environment variable `ENV_FOR_DYNACONF="production"` to make real requests to nasa api.
4. Run:
    ```shell
    $ poetry install
    $ uvicorn main:app
    ```
5. Go to [localhost:8000/apod](localhost:8000/apod)

## Testing
This project uses pytest.
```shell
$ pytest
```
