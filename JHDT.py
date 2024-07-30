import re

def is_valid_datetime(datetime_str):
# Regular expression pattern for ISO 8601 date-time format
  pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:\d{2})$&";
  return re.match(pattern, datetime_str) is not None

def read_datetime_values(file_path):
    with open(".\input.txt", "r") as file:
        datetime_values = read_datetime_values(file_path)
        print(datetime_values)  # Print the read values
        return datetime_values

def write_valid_datetime_values(datetime_values, output_file_path):
    valid_datetime_values = set()
    print("Valid date-time values:")
    for datetime_str in datetime_values:
        if is_valid_datetime(datetime_str):
            valid_datetime_values.add(datetime_str)
            print(datetime_str)  # Print each valid date-time value

    try:
        with open(".\\output1.txt", 'w') as output_file:
            for valid_datetime in valid_datetime_values:
                output_file.write(valid_datetime + '\n')
        print(f"Valid date-time values written to '.\\output1.txt'.")
    except Exception as e:
        print(f"Error writing to '.\\output1.txt': {e}")
