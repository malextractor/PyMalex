# File: pymalex.py
from typing import MutableMapping, Dict, Any
import logging
import requests
from urllib.parse import urljoin
import json

from .exceptions import PyMalexError, NoURL, NoKEY

PYMALEX_VERSION = "1.0.0"
logger = logging.getLogger('pymalex')

class PyMalex:
    """Python API for Malex

    :paran url: URL of the :alex instance you want to connect to
    :param key: API key you want to use
    :param ssl: Can be True or False (to check the validity of the certificate. Or a CA_BUNDLE in case of self signed or other certificate (the concatenation of all the crt of the chain)
    :param debug: Write all the debug information to stderr
    :param proxy: Proxy to use
    """

    def __init__(self, url: str, key: str, ssl: bool | str = True,
                 debug: bool = False, proxy: MutableMapping[str, str] | None = None):

        if not url:
            raise NoURL("Please provide the URL of your Malex instance.")
        if not key:
            raise NoKEY("Please provide your authorization key.")

        self.base_url: str = url
        self.key: str = key
        self.ssl: bool | str = ssl
        self.proxy: MutableMapping[str, str] | None = proxy

        self.logger = self._configure_logger(debug)

        try:
            malex_version = self._get_malex_version 
            if malex_version == PYMALEX_VERSION:
                self.logger.debug(f"You are using the same version: {malex_version}")
            else:
                self.logger.warning(f"You do not use the same version between the library and the server. Please use version {malex_version}, which is used by your server")
        except PyMalexError as e:
            raise e
        except Exception as e:
            raise PyMalexError(f'Unable to connect to Malex ({self.base_url}). Please make sure the API key and the URL are correct (http/https is required): {e}')

    def _configure_logger(self, debug: bool) -> logging.Logger:
        logger = logging.getLogger('pymalex')
        handler = logging.StreamHandler()
        
        if debug:
            logger.setLevel(logging.DEBUG)
            handler.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.WARNING)
            handler.setLevel(logging.WARNING)
        
        formatter = logging.Formatter('%(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not logger.handlers:
            logger.addHandler(handler)
        
        return logger

    def _request(self, method: str, route: str, params=None, data=None, headers=None):
        """Prepare and send a request with python-requests"""
        url = urljoin(self.base_url, route)
        response = requests.request(method, url, params=params, data=data, headers=headers)

        return response

    @property
    def _get_malex_version(self) -> str:
        """Returns the API version from the server"""
        malex_version = self._request("GET", "version")
        return malex_version.json()["version"]
