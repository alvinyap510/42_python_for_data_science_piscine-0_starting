from datetime import datetime

current_datetime = datetime.now()
unix_timestamp = current_datetime.timestamp()

print(
    f"Seconds since January 1, 1970: {format(unix_timestamp, ',.4f')} or {format(unix_timestamp, '.2e')} in scientific notation")
print(current_datetime.strftime('%b %d %Y'))
