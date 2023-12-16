from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print("Current Format", current_datetime)
# Format the date using "/"
formatted_date = current_datetime.strftime("%m/%d/%Y %H:%M:%S")

print("Formatted Date:", formatted_date)
