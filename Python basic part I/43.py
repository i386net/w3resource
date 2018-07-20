# 43. Write a Python program to get OS name,
# platform and release information.

import platform

print('OS name, platform and release information.')
# OS name
print('platform.system(): {}'.format(platform.system()))

#print('platform.machine: {}'.format(platform.machine()))
print('platform.platform(): {}'.format(platform.platform(aliased=True, terse=True)))
# platform release
print('platform.release(): {}'.format(platform.release()))
# macOS version
print('Returns macOS version: {}'.format(platform.mac_ver()[0]))
