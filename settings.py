# Configure global settings here
import os

# Configure Timeouts (Seconds)
GLOBAL_TIMEOUT = 10
IMPLICIT_WAIT = 10

API_TIMEOUT = 2
API_BASE_URL = ""
AUTH_TOKEN = os.environ["AUTH_TOKEN"] if "AUTH_TOKEN" in os.environ.keys() else None

# Paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
