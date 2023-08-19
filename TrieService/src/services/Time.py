from datetime import timezone
import datetime

def get_timestamp():
    dt = datetime.datetime.now(timezone.utc).timestamp()
    # utc_time = dt.replace(tzinfo=timezone.utc)
    # utc_timestamp = utc_time.timestamp()
    # return utc_timestamp
    return dt