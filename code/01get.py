import glob
import os
import shutil

for filename in glob.iglob('/opt/stata/ado/base/**/*.sthlp', recursive=True):
    print(filename)
    shutil.copy(filename, "../data/helpfiles/")
