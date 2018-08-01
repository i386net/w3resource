# 54. Write a Python program to get the current username

import os
import getpass

# Return the “login name” of the user.
print(os.getlogin())
print(getpass.getuser())
