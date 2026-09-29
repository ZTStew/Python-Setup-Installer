# Setup Installer
---
## Description:
Program is intended to simplify the execution of several .exe files that are to be run upon a computer having a new Windows OS installed on it by creating a single .exe file that runs all of the other .exe files

---
## Tasks:
- [ ] Create program to execute several .exe files in one go 
  - [x] Executables should all be stored in `New_Install_Package`
  - [x] Program can see the files it needs
  - [ ] Program can execute the files it needs
- [x] A file containing a list of files to execute should be added to `New_Install_Package`
- [x] Create program to quickly compile main program into .exe program


---
### Usage (export_exe.py):
(explanation of how to use the program)
1. Run `python export_exe.py`
2. "batch_setup.exe" will be found in `./compiled_program`

---
### Usage (batch_setup.exe):
(explanation of how to use the program)
1. Place "batch_setup.exe" into `\\server\Share\Apps`
2. Place files to be executed into `\\server\Share\Apps\New_Install_Package`

---
### ERRORS:
UNC paths are not supported.  Defaulting to Windows directory.
'New_Install_Package' is not recognized as an internal or external command,
operable program or batch file.
ERROR: on execution of: e-sword_1410_setup.exe |ERR| [WinError 740] The requested operation requires elevation
