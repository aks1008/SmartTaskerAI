import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment
base_url = os.getenv("API_BASE_URL")

def get_student_list():
    """
    Fetches the list of students.
    """
    if not base_url:
        raise ValueError("API_BASE_URL is not set in the environment variables.")

    response = requests.get(f"{base_url}students")


    if response.status_code == 200:
        data = response.json()  # or response.text for plain text
        return data
    else:
        print("Error:", response.status_code)