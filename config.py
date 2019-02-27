import os

# EDIT
USERNAME = 'pety.barczi@gmail.com'
PASSWORD = 'Lipovnik1@'
COURSES = [
        'learning-hadoop',
]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None
