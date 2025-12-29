"""
This test API simulates CRUD operations; actions do not actually modify the server data.
For more details, see the DummyJSON API documentation: https://dummyjson.com/docs/
"""

# Adding a new product will not add it into the server for this test API.
# It will simulate a POST request and will return the new created product with a new id
def test_add_product(api_client):
    keyboard_data = {
        "title": "Keyboard",
        "description": "test product",
        "category": "electronics",
    }
    response = api_client.post("/products/add", data=keyboard_data)
    data = response.json()
    assert response.status == 201, f"Expected 201 but got {response.status}"

    # Verify the added product matches what we expected
    assert data.get("title") == keyboard_data["title"], f"expected {keyboard_data['title']}, but got {data.get('title')}"
    assert data.get("description") == keyboard_data["description"], f"expected {keyboard_data['description']}, but got {data.get('description')}"
    assert data.get("category") == keyboard_data["category"], f"expected {keyboard_data['category']}, but got {keyboard_data['category']}"

    # Verify ID is autopopulated
    assert data.get("id") != "" and data.get("id") is not None, f"The added product should have an id, but got '{data.get('id')}'"


def test_get_product(api_client):
    product_id = 1
    expected_response = {
        "id": 1,
        "title": "Essence Mascara Lash Princess",
        "description": (
            "The Essence Mascara Lash Princess is a popular mascara known for its "
            "volumizing and lengthening effects. Achieve dramatic lashes with this "
            "long-lasting and cruelty-free formula."
        ),
        "category": "beauty",
    }
    response = api_client.get(f"/products/{product_id}")
    data = response.json()

    assert response.status == 200, f"Expected 200 but got {response.status}"
    assert data.get("id") == expected_response["id"], f"expected {expected_response["id"]}, but got {data.get('id')}"
    assert data.get("title") == expected_response["title"], f"expected {expected_response["title"]}, but got {data.get('title')}"
    assert data.get("description") == expected_response["description"], f"expected {expected_response["description"]}, but got {data.get('description')}"
    assert data.get("category") == expected_response["category"], f"expected {expected_response['category']}, but got {data.get('category')}"

# Updating a product will not update it into the server.
# It will simulate a PUT/PATCH request and will return updated product with modified data
def test_update_product(api_client):
    product_id_to_update = 1
    updated_product = {
        "title": "Keyboard",
        "description": "test updated product",
        "category": "electronics",
    }

    unchanged_fields = {
        "price": 9.99,
        "stock": 99,
        "discountPercentage": 10.48,
    }

    response = api_client.patch(f"/products/{product_id_to_update}", data=updated_product)
    data = response.json()

    assert response.status == 200, f"Expected 200 but got {response.status}"

    # Verify updated fields
    assert data.get("id") == product_id_to_update, f"expected {product_id_to_update}, but got {data.get('id')}"
    assert data.get("title") == updated_product["title"], f"expected {updated_product["title"]}, but got {data.get('title')}"
    assert data.get("description") == updated_product["description"], f"expected {updated_product["description"]}, but got {data.get('description')}"
    assert data.get("category") == updated_product["category"], f"expected {updated_product['category']}, but got {data.get('category')}"

    # Verify other fields were not updated
    assert data.get("price") == unchanged_fields['price'], f"expected {unchanged_fields['price']}, but got {data.get('price')}"
    assert data.get("stock") == unchanged_fields["stock"], f"expected {unchanged_fields["stock"]}, but got {data.get('stock')}"
    assert data.get("discountPercentage") == unchanged_fields["discountPercentage"], f"expected {unchanged_fields["discountPercentage"]}, but got {data.get('discountPercentage')}"


def test_update_product_that_does_not_exist(api_client):
    product_id_to_update = 195
    expected_response_message = f"Product with id '{product_id_to_update}' not found"
    updated_product = {
        "title": "Keyboard",
        "description": "test updated product",
        "category": "electronics",
    }

    response = api_client.patch(f"/products/{product_id_to_update}", data=updated_product)
    data = response.json()

    assert response.status == 404, f"Expected 200 but got {response.status}"
    assert data.get("message") == expected_response_message, f"Expected {expected_response_message} but got {data}"

# Deleting a product will not delete it into the server.
# It will simulate a DELETE request and will return deleted product with isDeleted & deletedOn keys
def test_delete_product(api_client):
    product_id = 1
    expected_response = {
        "id": 1,
        "title": "Essence Mascara Lash Princess",
        "isDeleted": True
    }
    response = api_client.delete(f"/products/{product_id}")
    data = response.json()

    assert response.status == 200, f"Expected 200 but got {response.status}"
    assert data.get("id") == expected_response["id"], f"expected {expected_response["id"]}, but got {data.get('id')}"
    assert data.get("title") == expected_response["title"], f"expected {expected_response["title"]}, but got {data.get('title')}"
    assert data.get("isDeleted") == expected_response["isDeleted"], f"expected {expected_response["isDeleted"]}, but got {data.get('isDeleted')}"
    assert data.get("deletedOn") != "" and data.get("deletedOn") is not None, "Date of deletion not found in response"

def test_search_for_product_that_does_not_exist(api_client):
    product_name = "keyboard"
    expected_response = {
        "products": [],
        "total": 0,
        "skip": 0,
        "limit": 0,
    }
    response = api_client.get(f"/products/search?q={product_name}")
    data = response.json()

    assert response.status == 200, f"Expected 200 but got {response.status}"
    assert data == expected_response, f"Expected {expected_response} but got {data}"

def test_search_for_product_by_id_that_does_not_exist(api_client):
    product_id = 195
    expected_response_message = f"Product with id '{product_id}' not found"
    response = api_client.get(f"/products/{product_id}")
    data = response.json()

    assert response.status == 404, f"Expected 404 but got {response.status}"
    assert data.get("message") == expected_response_message, f"Expected {expected_response_message} but got {data}"