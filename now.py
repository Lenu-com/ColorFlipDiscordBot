from typing import Final
from datetime import datetime

def fetch_now() -> None:
    now = datetime.now()
    return now.strftime('%Y%m%d%H%M%S')