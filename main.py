
import os
import glob
import subprocess

# Specify the path to your repository (folder)
repo_path = os.getcwd() + '/scripts'

# Change the working directory to the repository
os.chdir(repo_path)

# Get all Python files in the repository
python_files = glob.glob("*.py")

file_num = 0
running = True


while running:
    file_num = 0
    for file in python_files:

        print(file_num,"-",file)
        file_num+=1


    file_choice=int(input("Pick number a to run a file, or pick a larger number to exit: "))

    if(file_choice>=len(python_files)):
        print("Exiting....")
        running = False
    else:
        print("Selected: ", python_files[file_choice])
        subprocess.run(["python3", python_files[file_choice]], check=True)