import os
import sys

print('This program will replace config files of the apps listed with the settings stored here')
print('It is recommended to perform a backup before proceeding')


# Terminate the program if it isn't running on linux
if(not (sys.platform == 'linux')):
    sys.exit()

# Check if ~/.config exists, if it doesn't create it
if (os.path.isdir(os.path.expanduser('~') + '/.config') == False) :
    os.system('mkdir ~/.config')


# Copy config files
os.system('cp -r config/alacritty/ ~/.config/alacritty')
os.system('cp -r config/picom/ ~/.config/picom')
os.system('cp -r config/ranger/ ~/.config/ranger')
os.system('cp -r config/xmobar/ ~/.config/xmobar')
os.system('cp -r config/xmonad/ ~/.')
os.system('cp config/.xinitrc ~/.xinitrc')


# Copy fonts
os.system('cp -r fonts/ ~/.fonts/')
