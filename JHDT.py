import re

def is_valid_datetime(datetime_str):
# Regular expression pattern for ISO 8601 date-time format
  pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})$&";
  return re.match(pattern, datetime_str) is not None

def read_datetime_values(file_path):
  try:
    with open('C:/Users/Jerome/Desktop/wtpython/input.txt', "r") as file:
      datetime_values = file.read().splitlines()
      return datetime_values
  except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    return []

def write_valid_datetime_values(datetime_values, output_file_path):
  valid_datetime_values = set()
  print("Valid date-time values:")
  for datetime_str in datetime_values:
    if is_valid_datetime(datetime_str):
       valid_datetime_values.add(datetime_str)
    try:
      with open("C:/Users/Jerome/Desktop/wtpython/output.txt", 'w') as output_file:
        for valid_datetime in valid_datetime_values:
          output_file.write(valid_datetime + '\n')
      print(f"Valid date-time values written to 'C:/Users/Jerome/Desktop/wtpython/output.txt'.")
    except Exception as e:
      print(f"Error writing to 'C:/Users/Jerome/Desktop/wtpython/output.txt': {e}")
