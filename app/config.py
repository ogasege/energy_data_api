# config.py

import os

# Use environment variables or hardcoded values
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:password@localhost/energy_data_db")