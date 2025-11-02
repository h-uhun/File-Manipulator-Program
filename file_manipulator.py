import sys
import os

def fileMissingCheck(fp):
    if not os.path.exists(fp):
        print('File is not exists: ' + fp)
        print('Please specify a different filename.')
        sys.exit()

def fileExistCheck(fp):
    if os.path.exists(fp):
        print('File exists: ' + fp)
        print('Please specify a different filename.')
        sys.exit()

errorMessage = """
Please enter a command
Command List
"reverse inputpath outputpath" : Create a new file in the output path with the contents of the input path reversed.
"copy inputpath outputpath" : Create a copy of the file located in inputpath and save it as outputpath.
"duplicate-contents inputpath n" : Copy the contents of inputpath and write the copied contents to inputpath n times.
"replace-string inputpath needle newstring" : Search for the string "needle" within the contents of the file located at inputpath,and replace all occurrences of "needle" with "newstring"
"""

if(len(sys.argv) == 4):
    if(sys.argv[1] == 'reverse'):
        ip = sys.argv[2]
        op = sys.argv[3]
        fileMissingCheck(ip)
        fileExistCheck(op)
        contents = ''
        with open(ip) as f:
            contents = f.read()
        with open(op, 'x') as f:
            f.write(contents[::-1])
    elif(sys.argv[1] == 'copy'):
        ip = sys.argv[2]
        op = sys.argv[3]
        fileMissingCheck(ip)
        fileExistCheck(op)
        contents = ''
        with open(ip) as f:
            contents = f.read()
        with open(op, 'x') as f:
            f.write(contents)
    elif(sys.argv[1] == 'duplicate-contents'):
        ip = sys.argv[2]
        n = sys.argv[3]
        fileMissingCheck(ip)
        if(not n.isdigit()):
            print('n is not number.')
            print('Please enter the number of copies you wish to make.')
            sys.exit()
        contents = ''
        with open(ip) as f:
            contents = f.read()
        with open(ip, 'a') as f:
            for i in range(int(n)):
                f.write(contents)
    else:
        print(errorMessage)
elif (len(sys.argv) == 5):
    if(sys.argv[1] == 'replace-string'):
        ip = sys.argv[2]
        fileMissingCheck(ip)
        n = sys.argv[3]
        ns = sys.argv[4]
        contents = ''
        with open(ip) as f:
            contents = f.read()
        with open(ip, 'w') as f:
            f.write(contents.replace(n, ns))
    else:
        print(errorMessage)
else:
    print(errorMessage)