import sys
import subprocess

nbfilename = sys.argv[1]

#finally run the stuff
if nbfilename == '':
    raise AssertionError("cant be empty")
subprocess.run(f'''jupytext --set-kernel "julia-1.10" --execute {nbfilename}''', shell=True, check=True)
