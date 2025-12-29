import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


assert BASE_URL, "BASE_URL must be set"
assert USERNAME, "USERNAME must be set"
assert PASSWORD, "PASSWORD must be set"
