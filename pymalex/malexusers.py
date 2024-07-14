# File: malexusers.py
from typing import Dict, Any
import json

from .pymalex import PyMalex

class MalexUsers:
    """Class to handle users in Malex"""

    def __init__(self, pymalex: PyMalex):
        self.pymalex = pymalex

    def list_users(self) -> Dict[str, Any]:
        """List all users"""
        response = self.pymalex._request("GET", "users")
        return response.json()

    def add_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new user"""
        response = self.pymalex._request("POST", "users", data=json.dumps(user_data), headers={"Content-Type": "application/json"})
        return response.json()

    def modify_user(self, user_id: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Modify an existing user"""
        route = f"users/{user_id}"
        response = self.pymalex._request("PUT", route, data=json.dumps(user_data), headers={"Content-Type": "application/json"})
        return response.json()

    def delete_user(self, user_id: str) -> Dict[str, Any]:
        """Delete a user"""
        route = f"users/{user_id}"
        response = self.pymalex._request("DELETE", route)
        return response.json()

    def get_user(self, user_id: str) -> Dict[str, Any]:
        """View an existing user"""
        route = f"users/{user_id}"
        response = self.pymalex._request("GET", route)
        return response.json()