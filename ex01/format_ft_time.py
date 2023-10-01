from datetime import datetime

current_datetime = datetime.now()
unix_timestamp = current_datetime.timestamp()

print(
    "Seconds since January 1, 1970: " +
    f"{format(unix_timestamp, ',.4f')}" +
    " or " +
    f"{format(unix_timestamp, '.2e')}" +
    " in scientific notation")
print(current_datetime.strftime('%b %d %Y'))
