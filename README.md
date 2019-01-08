# WindowsSiteBlockerPY
A simple PY script that messes with the "hosts" file on Windows and block websites! :)

This python script must be run as ROOT/ADMIN. You can also make an .exe of it using pyintaller library (also must run as ADMIN/ROOT):

pip install pyinstaller

pytinstaller --nowindowed --onefile WebBlocker.py (--nowindowed will allow a cmd window to open for the user to insert data; --onefile will make just one .exe file in the "Dist" folder and it´s ready to run (else it would make an .exe + extension files on a folder). 
