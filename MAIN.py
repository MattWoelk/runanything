import os
import subprocess

path = os.environ['PATH']
paths = path.split(':')
programs = [] # List of all programs which could be auto-completed
              # TODO: make it a dict with the corresponding path or something

for i in paths:
  programs += os.listdir(i)

#print(programs)







## Useful tools which may be useful to me later on in development:

# This is used to launch a program in a new terminal which runs independently from this python program
#subprocess.Popen (['urxvt', '-e', 'sleep', '1']) 

# This is used to launch a program which this python program waits for
#os.system('''urxvt -e sleep 3''')
