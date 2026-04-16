from app import create_app


def test_home_page_displays_main_message():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Hola Mundo desde DevOps CI/CD" in response.data


def test_health_endpoint_returns_expected_payload():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Hola Mundo desde DevOps CI/CD",
        "status": "ok",
    }
