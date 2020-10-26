import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
# default to the example if the .env doesn't exist
# if os.path.isfile(env_path):
load_dotenv()

DEBUG = bool(int(os.getenv("DEBUG")))
USE_DEBUGGER = bool(int(os.getenv("USE_DEBUGGER")))
USE_RELOADER = bool(int(os.getenv("USE_RELOADER")))