import os

PATH = r'venv'

Nfiles = 0
Ndir = 0

for root, dirnames, filenames in os.walk(PATH):
    Nfiles += len(filenames)
    Ndir += len(dirnames)

print(Nfiles, Ndir)