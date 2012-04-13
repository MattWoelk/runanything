import os
import subprocess

paths = os.environ['PATH'].split(':')
programs = [] # List of all programs which could be auto-completed

for i in paths:
  programs += os.listdir(i)

# change the for loop to do an insertion sort (with a placeholder; super efficient) so the list is in order.
# maybe to start just use the "sort" function
programs = sorted(programs, key=str.lower) #success!
print(programs)


# TODO: make it a dictionary (tuples?) with the corresponding path or something
# TODO: Interface with qt
# TODO: - get input from the keyboard every time a key is hit
# TODO: - check to see if there are any matches
# TODO: - if so, show them in a list which key-bindings will highlight






## Useful tools which may be useful to me later on in development:

# This is used to launch a program in a new terminal which runs independently from this python program
#term = os.environ['TERM'] # this is actually useless, (we can't run it from this information) so we'll have to set it in a config file :P
#subprocess.Popen (['urxvt', '-e', 'sleep', '1']) 

# This is used to launch a program which this python program waits for
#os.system('''urxvt -e sleep 3''')
