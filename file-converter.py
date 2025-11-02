import markdown
import sys
import os

def fileMissingCheck(fp):
    if not os.path.exists(fp):
        print('File does not exists: ' + fp)
        print('Please specify a different filename.')
        sys.exit()

def fileExistCheck(fp):
    if os.path.exists(fp):
        print('File exists: ' + fp)
        print('Please specify a different filename.')
        sys.exit()

errorMessage = """
Please enter a command
markdown inputfile outputfile : Converts Markdown(inputfile) to HTML(outputfile) and outputs it.
"""

if(len(sys.argv) == 4):
    if(sys.argv[1] == 'markdown'):
        ip = sys.argv[2]
        op = sys.argv[3]
        fileMissingCheck(ip)
        fileExistCheck(op)
        text = ''
        with open(ip, 'r', encoding='utf-8') as f:
            text = f.read()
        html = markdown.markdown(text)
        with open(op, 'x', encoding='utf-8', errors='xmlcharrefreplace') as f:
            f.write(html)
    else:
        print(errorMessage)
else:
    print(errorMessage)
