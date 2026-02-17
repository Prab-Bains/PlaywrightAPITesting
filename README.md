# Playwright API Testing

A backend API test suite built with Playwright and Python. This project was put together to demonstrate comfort with API testing concepts and the Playwright framework — not to be an exhaustive test suite, but to show how I'd approach backend testing in a real-world context.

---

## Project Structure

```
PlaywrightAPITesting/
├── config/         # Configuration and environment settings
├── tests/          # Test files
├── utils/          # Helper functions and shared utilities
├── pytest.ini      # Pytest configuration
└── requirments.txt # Dependencies
```

---

## What's Tested

The test suite covers core CRUD operations against the DummyJSON API, focusing on:

- **GET** requests — verifying response status, structure, and data correctness
- **POST** requests — creating resources and asserting the response reflects what was sent
- **PUT/PATCH** requests — updating resources and confirming changes
- **DELETE** requests — removing resources and checking appropriate status codes
- **Status code validation** — making sure the API returns the right codes for both success and error cases
- **Response body assertions** — checking that response payloads match expected schemas and values

---

## Setup

**Requirements:** Python 3.10+

```bash
# Clone the repo
git clone https://github.com/Prab-Bains/PlaywrightAPITesting.git
cd PlaywrightAPITesting

# Install dependencies
pip install -r requirements.txt

# Install Playwright
playwright install
```

---

## Running the Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/<test_file>.py
```

HTML reports are generated automatically via Playwright's built-in reporter.

---
