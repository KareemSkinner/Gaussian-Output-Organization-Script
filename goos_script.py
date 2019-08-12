# this script reads Gaussian .log files located in its folder. Writes the file name, physical parameters, and the Sum of electronic and thermal Free Energies to an output file
# makes getting this data through Gaussian .log files a lot quicker

import os # for working with filenames 
import re # regex library

output_file = open("python_script_output.txt", "a+")

print("Working on files...")

currentDirectory = os.getcwd()  # gets present working directory
for filename in os.listdir(currentDirectory):
        try:
            if filename.endswith(".log"):
                input_file = open(filename, "r")
                print(filename, file = output_file)
                current_file = input_file.readlines()

                for input_line in current_file:
                    datastring = "Sum of electronic and thermal Free Energies".lower()

                    if input_line.lower().find("temperature" and "kelvin" and "pressure") != -1:
                        print(input_line, file = output_file)
                    if input_line.lower().find(datastring) != -1:
                        print(input_line, file = output_file)
        except Exception as noFile:
            raise noFile
            print ("No files found here...")

print("Data retrieval complete.")

input_file.close()
output_file.close()

input("Press Enter to exit...")
