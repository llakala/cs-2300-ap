from datetime import datetime

# Pre-defined date string
date_str = "2022-03-17 10:45:30"
# Convert data string to date obj, in Y, m, d, H, M, S format
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
# takes a formatted date object and converts it into a formatted date string
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# Print formatted string
print(formatted_date)
