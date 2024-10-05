import sys
import platform
import sysconfig
import platform

#This program just prints the current python version in different ways
#https://stackoverflow.com/questions/1252163/printing-python-version-in-output
print()
print("sys.version : " + sys.version)
print()
print("platform.python_version() : " + platform.python_version())
print()
print("sysconfig.get_python_version() : " + sysconfig.get_python_version())
print()
print("sys.version_info : " , sys.version_info)
print()
print("via platform python_build()" ,  platform.python_build())