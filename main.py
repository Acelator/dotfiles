import os
import sys

# Terminate the program if it isn't running on linux
if sys.platform != 'linux':
    sys.exit()


def ask_for_confirmation(text):
    confirmation = str(input(text))
    if confirmation == 'y':
        return True
    else:
        return False


print('This program will replace config files of the apps listed with the settings stored here')
print('It is recommended to perform a backup before proceeding')
print('Right now only pacman is only supported as package manager')

START = ask_for_confirmation('Start? (y or n): ')
if START is False:
    print('Aborting')
    sys.exit()
print('Starting....')

# Install package
print('Installing packages....')
try:
    os.system('sudo -S pacman -S --needed git xorg-server xorg-apps xorg-xinit xorg-xmessage libx11 libxft libxinerama libxrandr libxss pkgconf')
    os.system('sudo -S pacman -S alacritty ranger xmonad xmobar xmonad-contrib dmenu zsh feh xscreensaver --needed')
except:
    print('Errorr')

try:
    os.system('paru -S picom-jonaburg-git')
except:
    print('Error installing picom through paru')

# Setting up zsh
print('Installing oh-my-zsh')
print('Exit the zsh terminal once oh-my-zsh is intalled to continue the scripts')

os.system('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')

# Copy config files
print('Copying config files')

# Check if ~/.config exists, if it doesn't create it
if os.path.isdir(os.path.expanduser('~') + '/.config') is False:
    os.system('mkdir ~/.config')

os.system('cp -r config/alacritty/ ~/.config/alacritty')
os.system('cp -r config/picom/ ~/.config/picom')
os.system('cp -r config/ranger/ ~/.config/ranger')
os.system('cp -r config/xmobar/ ~/.config/xmobar')
os.system('cp -r config/.xmonad/ ~/.')
os.system('cp config/.xinitrc ~/.xinitrc')

# Configure zsh
os.system('cp config/zsh/.zshrc ~/.zshrc')
os.system('cp -r config/zsh/.oh-my-zsh/themes/ ~/.oh-my-zsh/custom/')

# zsh plugins (maybe install themes directly from GitHub)
os.system(
    'git clone https://github.com/zsh-users/zsh-autosuggestions ${'
    'ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions')
os.system('git clone https://github.com/supercrabtree/k ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/k')

# Copy fonts
print('Setting up fonts')
os.system('cp -r fonts/ ~/.fonts/')

# Set up Background
os.system('curl https://i.imgur.com/zYq9vdC.jpeg > 1a.jpeg')

if os.path.isdir(os.path.expanduser('~') + '/Pictures') is False:
    os.system('mkdir ~/Pictures')

if os.path.isdir(os.path.expanduser('~') + '/Pictures/wallpapers') is False:
    os.system('mkdir ~/Pictures/wallpapers')

os.system('mv 1a.jpeg ~/Pictures/wallpapers/1a.jpeg')
