""" This script reads Gaussian .log files located in its folder. 
    Writes the file name, physical parameters, and the Sum of electronic and thermal Free Energies to an output file
    Makes getting this data through Gaussian .log files a lot quicker
""" 

import os 
import re 

output_file = open("python_script_output.txt", "a+")
print("Working on files...")
currentDirectory = os.getcwd()      # gets present working directory

for filename in os.listdir(currentDirectory):   # loops through each file in current directory
    if filename.endswith(".log"):
        try:
            with open(filename, "r") as input_file:     # handles closing of every input file opened
                print(filename, file = output_file)
                print("----------------------------------------------------------------------------------------", file = output_file) # separates outputs of each file
                current_file = input_file.readlines()
                parameterstring = "temperature="                                        # extracts parameters used in Gaussian log
                datastring = "Sum of electronic and thermal Free Energies".lower()      # extracts specific line of desired data in Gaussian log 
                for input_line in current_file:     # loops through each line in current file
                    if input_line.lower().find(parameterstring) != -1:
                        print(input_line, file = output_file)
                    if input_line.lower().find(datastring) != -1:
                        print(input_line, file = output_file)
        except IOError as noFile:
            print ("No files found here...")
            raise noFile       
print("Data retrieval complete.")
output_file.close()

input("Press Enter to exit...")