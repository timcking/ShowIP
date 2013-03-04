@echo off
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q Output
python setup.py py2exe
rem istool -compile LoadTempTables.iss
