"""
Description: 
  Program takes a list of executables found in `programs_file` and runs them automatically 
  with a single run of the program.
  The intent is to speed up and increase accuracy of programs being installed on a fresh install 
  of a .iso image

  If new programs need to be added to the execution process:
    Place the program (.exe or .bat) into `programs_file`
    In "[programs_file]/Install_List/install_list.ini", in "install_targets" add the name of the program
    including the extention of the program and seperated from the other programs listed by a ","
Compatibility:
  Works only with Windows

Author: Zachary Stewart
"""


import os, configparser, shutil, subprocess, asyncio


async def main():
  # sets location where executables are to be stored
  programs_file = "New_Install_Package"
  # gets relative location of cmd.exe
  cmd = shutil.which("cmd.exe")

  # 
  config = configparser.ConfigParser()
  config.read('./New_Install_Package/Install_List/install_list.ini')
  install_list = config["install_list"]["install_targets"]
  # print(install_list)
  install_list = install_list.split(",")
  
  processes = []

  try:
    # loops through list of files to be executed
    for program in install_list:
      # sanitizes user input
      program = program.strip()
      # builds path to program to be executed
      execute_program = programs_file + "/" + program

      # checks if program given by user is a .bat file
      if program.lower().endswith(".bat"):
        # runs .bat files
        process = subprocess.Popen([cmd, "/c", execute_program])
      else:
        # runs .exe files
        process = subprocess.Popen([execute_program])
        # version that open a terminal for each .exe program
        # process = subprocess.Popen([execute_program], creationflags=subprocess.CREATE_NEW_CONSOLE)

      # adds execution script to `processes` to be executed
      processes.append(process)

    # runs each process
    for process in processes:
      process.wait()
  except Exception as e:
    print("ERROR: on execution of: " + program + " |ERR| " + str(e))


if __name__ == "__main__":
  # calling the main function
  asyncio.run(main())
  # remove line from final product
  input("\nPress Enter to exit...")