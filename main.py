import os
import sys

# Terminate the program if it isn't running on linux
if sys.platform != 'linux':
    sys.exit()


def askForConfirmation(text):
    confirmation = str(input(text))
    if confirmation == 'y':
        return True
    else:
        return False


print('This program will replace config files of the apps listed with the settings stored here')
print('It is recommended to perform a backup before proceeding')
print('Right now only pacman is only supported as package manager')


start = askForConfirmation('Start? (y or n): ')
if start is False:
    print('Aborting')
    sys.exit()
print('Starting....')

#TODO: Install x-org related utilities?

# Install package
print('Installing packages....')
try:
    os.system('sudo -S pacman -S alacritty ranger xmobar xmonad zsh')
except:
    print('Errorr')


# Setting up zsh
print('Installing oh-my-zsh')
os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
setAsdefaultShell = askForConfirmation('Should zsh be set up as the default shell? (y or n): ')
if setAsdefaultShell == True:
    os.system('chsh -s $(which zsh)')


# Copy config files
print('Copying config files')

# Check if ~/.config exists, if it doesn't create it
if os.path.isdir(os.path.expanduser('~') + '/.config') is False :
    os.system('mkdir ~/.config')

os.system('cp -r config/alacritty/ ~/.config/alacritty')
os.system('cp -r config/picom/ ~/.config/picom')
os.system('cp -r config/ranger/ ~/.config/ranger')
os.system('cp -r config/xmobar/ ~/.config/xmobar')
os.system('cp -r config/xmonad/ ~/.')
os.system('cp config/.xinitrc ~/.xinitrc')

os.system('cp config/zsh/.zshrc ~/.zshrc')
os.system('cp -r config/zsh/.oh-my-zsh/themes ~/.oh-my-zsh/custom')

# Copy fonts
print('Setting up fonts')
os.system('cp -r fonts/ ~/.fonts/')
