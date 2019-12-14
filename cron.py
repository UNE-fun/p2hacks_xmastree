from datetime import datetime
from app import tweets_at

date_str = datetime.now().isoformat(timespec="seconds")
tweets_at(date_str)
