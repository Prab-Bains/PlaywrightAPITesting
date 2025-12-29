from utils.auth import login

def test_login_with_valid_credentials(api_client):
    response = login(api_client)
    expected_keys = {
        "id",
        "username",
        "email",
        "firstName",
        "lastName",
        "gender",
        "image",
        "accessToken",
        "refreshToken",
    }

    # Verify successful request
    assert response.status == 200, "Authentication failed"

    data = response.json()

    # Verify response is correct and not missing any data
    for key in expected_keys:
        assert key in data.keys(), f"Missing field: {key}"
        assert data.get(key) is not None, f"{key} is None"
        assert data.get(key) != "", f"{key} is empty"
        if key == "id":
            assert isinstance(data.get(key), int)
        else:
            assert isinstance(data.get(key), str)

    # Verify each of the values look correct and not empty
    assert "@" in data.get("email"), "Email is invalid"
    assert data.get("gender") in ["male", "female"]
    assert data.get("image").startswith("https://")

    # Verify JWT tokens contain header, payload, and signature
    assert data.get("accessToken").count(".") == 2
    assert data.get("refreshToken").count(".") == 2


def test_login_with_invalid_credentials(api_client):
    request = {
        "username": "invalidUsername",
        "password": "invalidPassword",
        "credentials": 'include'
    }

    response = api_client.post("/auth/login", data=request)

    data = response.json()

    assert data.get("message") == "Invalid credentials"
    assert response.status == 400

def test_login_with_missing_credentials(api_client):
    data = {
        "headers": {'Content-Type': 'application/json'},
        "username": "invalidUsername",
        "credentials": 'include'
    }

    response = api_client.post("/auth/login", data=data)

    data = response.json()

    assert data.get("message") == "Username and password required"
    assert response.status == 400
