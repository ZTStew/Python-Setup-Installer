"""
Description:
Program compiles the existing project and moves the results into a readied package for export
"""

import os, shutil, subprocess

# name of export ready folder
export_folder = './compiled_program'
errors = []


"""
compiles program for export
"""
# command to compile program
# remove "--console" from final product
command = [
    "pyinstaller",
    "--onefile",
    "-w",
    "--console",
    "batch_setup.py"
]

subprocess.run(command, check=True)


# removes unnessisary directory
try:
  shutil.rmtree('./build')
except Exception as e:
  errors.append("removes ./build " + str(e))

# removes unnessisary file
try:
  os.remove("./batch_setup.spec")
except Exception as e:
  errors.append("removes .spec file " + str(e))


"""
Moves files into export folder
"""
# makes export folder
try:
  os.makedirs(export_folder)
except Exception as e:
  errors.append("makes export folder " + str(e))

# moves .exe file into export folder
# renames .exe file into something more user friendly
try:
  # removes old program in case it is still present
  try:
    os.remove(export_folder + "/batch_setup.exe")
  except Exception as e:
    errors.append("removes old executable " + str(e))
  shutil.move("./dist/batch_setup.exe", export_folder + "/batch_setup.exe")
except Exception as e:
  errors.append("moves .exe to `compiled_program` and renames it " + str(e))


# removes unnessisary directory
try:
  shutil.rmtree('./dist')
except Exception as e:
  errors.append("removes ./dist, an unnessisary directory " + str(e))


print("Export Complete")
print("ERRORS: " + str(errors))
