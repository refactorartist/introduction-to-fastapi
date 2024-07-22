# Project Title

## Description

This project showcases basic CRUD (Create, Read, Update, Delete) operations using FastAPI. It is designed solely for educational purposes to demonstrate how to implement these fundamental operations in a RESTful API.


## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed the latest version of [PDM](https://pdm.fming.dev/), a modern Python package manager with PEP 582 support. PDM is used to manage the project's dependencies and package installation.
- Tools like [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/) will be required to test the endpoints and interact with the API.
- As an alternative, just navigate to http://127.0.0.1/docs after running the instructions in `Starting the Project`

## Starting the Project

To begin working with the project, follow these steps:

1. Clone the project repository to your local machine:

    Using HTTPS 

    ```bash
    git clone https://github.com/refactorartist/introduction-to-fastapi.git
    ```

    Alternatively, using SSH 

    ```bash
    git clone git@github.com:refactorartist/introduction-to-fastapi.git
    ```

2. Navigate to the Project 

    ```bash
    cd introduction-to-fastapi
    ```

3. Install the Project 

    ```bash
    pdm install
    ```

4. Run the server 
    
    ```bash
    pdm run server
    ```

5. Open the Documentation
    
    In your favorite browser, navigate to http://127.0.0.1/docs to try out the various endpoints

    Alternatively, you can use [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/) instead

## Linting 

To ensure the project is properly linted, run the following command

```bash
pdm run lint
```

The project uses [ruff](https://github.com/astral-sh/ruff) for linting

## Type Checks

The project uses mypy for static analysis. Checkout [mypy](https://www.mypy-lang.org/)

To run mypy, run the following 

```bash
pdm run typecheck
```