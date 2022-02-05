# OpenAPI generated FastAPI server

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.7.2
- Build package: org.openapitools.codegen.languages.PythonFastAPIServerCodegen

## Requirements.

Python >= 3.7

## Installation & Usage

To run the server, please execute the following from the root directory:

```bash
pip3 install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8080
```

and open your browser at `http://localhost:8080/docs/` to see the docs.

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
docker-compose up --build
```

## Tests

To run the tests:

```bash
pip3 install pytest
PYTHONPATH=src pytest tests
```
