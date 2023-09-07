import requests
import certifi
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Sending a GET request to www.example.com...")
try:
    response = requests.get('https://www.example.com', verify=certifi.where())
    logger.info("Request to www.example.com was successful!")
except Exception as e:
    logger.error("Failed to make a request to www.example.com: %s", e)
python-tk
watchmen
python3.11