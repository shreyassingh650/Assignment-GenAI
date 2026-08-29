#task 6 Read File Safely (Error Handling Inside File Handling Only)
import os
file_path = input("Enter The File Path:\n")

if os.path.exists(file_path):
    with open(file_path,'r') as f:
        print(f.read())
else:
    print('File not found. Please check the filename')