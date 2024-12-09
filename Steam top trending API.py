import os
from steam_web_api import Steam

KEY = os.environ.get("4DC6F9BA5AE6D2FE1405F7E01A4EB137")

steam = Steam(KEY)

steam.users.search_user("the12thchairman")