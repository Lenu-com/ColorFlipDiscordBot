from datetime import datetime


def fetch_now() -> str:
    now = datetime.now()
    return now.strftime('%Y%m%d%H%M%S')

