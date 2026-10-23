# Section 2.1

# 1. git is a place to store files and github is where to upload
# 2. the terminal is the place to write code and the place to write your commands in on the command line, the command line is within it
# 3. repositories are places to store your code, local is within your computer and remote is somewhere diff like github
# 4. vc stores data
# 5. place where you preview the things you want to upload to git before you do
# 6. adds files to staging area
# 7. saves files in staging area
# 8. launches files to github from staging area
# 9. displays current status of file 
# 10. takes files from remote repo 
# 11. prints the path of directory and how u got there
# 12 lists files within a dir 
# 13. change directory
# 14. opens code editor
# 15. creates new code file
# 16. moves files to diff directory
# 17. deletes files
# 18. displays contents of file without editing 

# Section 2.2

# 1. pwd
# 2. ls 
# 3. cd ../brianna_repo, git pull
# 4. mv homework.py ../judy_decal/homework/
# 5. cd ../judy_decal/homework/
# 6. cat homework.py
# 7. 
# git add .
# git commit -m "finished homework"
# git push origin main 
# 8.
# cd ..
# git pull origin main
# git push origin main
# The error means the remote repository has changes
# that Judy does not have locally. She needs to pull
# those changes before pushing her own.
# 9. cd~/Recents/

#Section 3.1

def checktype(value):
    if type(value) == int:
        return "int"
    if type(value) == float:
        return "float"
    if type(value) == str:
        return "str"
    if type(value) == bool:
        return "boolean"
# Section 3.2
def evenOrOdd(value):
    if value % 2 == 1:
        return "odd"
    if value % 2 == 0:
        return "even"

# Section 4
def sumWithLoop(numbers):
    total = 0
    for x in numbers: 
        total = total + x
    return total 

# Section 5.1
def duplicateList(items):
    new_list = []
    for item in items: 
        new_list.append(item)
        new_list.append(item)
    return new_list

# Section 5.2
def square(num):
    return num * num

# Section 6.2

print(evenOrOdd(10))