from datetime import datetime, timedelta

with open("C:/Users/Jerome/Desktop/wtpython/input.txt", "r") as f:
    content = f.readlines()
    print(content)

file_name = str(content)    
with open("C:/Users/Jerome/Desktop/wtpython/output.txt", "w") as f:
    f.write(file_name + '\n')
    f.close()
