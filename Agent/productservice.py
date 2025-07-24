import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment
base_url = os.getenv("PRODUCT_BASE_URL")

def get_shopping_list():
    """
    Fetches the item list present in inventory with item name, price, and category.
    """
    if not base_url:
        raise ValueError("PRODUCT_BASE_URL is not set in the environment variables.")

    response = requests.get(f"{base_url}shoppinglist")

    if response.status_code == 200:
        data = response.json()  # or response.text for plain text
        return data
    else:
        print("Error:", response.status_code)

def get_user():
    """
    Fetches user details like username, email and balance.
    """
    if not base_url:
        raise ValueError("PRODUCT_BASE_URL is not set in the environment variables.")

    response = requests.get(f"{base_url}users")

    if response.status_code == 200:
        data = response.json()  # or response.text for plain text
        return data
    else:
        print("Error:", response.status_code)

def get_shopping_list_user():
    """
    Fetches shopping list for user, which user what purchased and how much total cart amount.
    """
    if not base_url:
        raise ValueError("PRODUCT_BASE_URL is not set in the environment variables.")

    response = requests.get(f"{base_url}shoppinglistuser")

    if response.status_code == 200:
        data = response.json()  # or response.text for plain text
        return data 
    else:
        print("Error:", response.status_code)
