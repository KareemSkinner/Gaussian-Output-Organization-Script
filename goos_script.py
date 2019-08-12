import os, re

input_file = open("acetaldehyde.log", "r")
input_file_name = os.path.basename(input_file.name)

datastring = "Sum of electronic and thermal Free Energies".lower()

output_file = open("python_script_output.txt", "a+")

file = input_file.readlines()

print("Working on file...")

print(input_file_name, file = output_file)
for input_line in file:
    if input_line.lower().find("temperature" and "pressure" and "connectivity") != -1:
        print(input_line, file = output_file)
    elif input_line.lower().find(datastring) != -1:
        print(input_line, file = output_file)
print("File completed")

input_file.close()
output_file.close()

input("Press Enter to exit...")
