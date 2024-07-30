from datetime import datetime, timedelta

with open(".\input.txt", "r") as f:
    content = f.readlines()
    print(content)

file_name = str(content)    
with open(".\output.txt", "w") as f:
    f.write(file_name + '\n')
    f.close()
