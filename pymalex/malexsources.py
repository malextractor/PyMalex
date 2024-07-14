# File: malexsources.py
from typing import Dict, Any
import json

from .pymalex import PyMalex

class MalexSources:
    """Class to handle sources in Malex"""

    def __init__(self, pymalex: PyMalex):
        self.pymalex = pymalex

    def list_sources(self) -> Dict[str, Any]:
        """List all sources"""
        response = self.pymalex._request("GET", "sources")
        return response.json()

    def add_source(self, source_data: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new source"""
        response = self.pymalex._request("POST", "sources", data=json.dumps(source_data), headers={"Content-Type": "application/json"})
        return response.json()

    def modify_source(self, source_id: str, source_data: Dict[str, Any]) -> Dict[str, Any]:
        """Modify an existing source"""
        route = f"sources/{source_id}"
        response = self.pymalex._request("PUT", route, data=json.dumps(source_data), headers={"Content-Type": "application/json"})
        return response.json()

    def delete_source(self, source_id: str) -> Dict[str, Any]:
        """Delete a source"""
        route = f"sources/{source_id}"
        response = self.pymalex._request("DELETE", route)
        return response.json()
