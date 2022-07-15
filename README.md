# xcampy
Raspberry Pi camera package

#R Pi Setup
sudo apt update
sudo apt full-upgrade

export PATH=$PATH:/home/neptune/.local/bin
source ~/.bashrc

## GitHub
ssh-keygen -t ed25519 -C "your_email@example.com"

## Virtual Environments
pip3 install virtualenv virtualenvwrapper
nano ~/.bashrc

#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin

source ~/.bashrc

mkvirtualenv xcampy --system-site-packages
workon xcampy
deactivate


lsvirtualenv -b -l
rmvirtualenv xcampy


pip freeze


# Install XCamPy
pip3 install -e .[develop]
pip install your-package --no-cache-dir

export PATH=$PATH:/path/you/want/to/add
/home/neptune/.local/bin

pip freeze | xargs pip uninstall -y

#VS Code
sudo apt update
sudo apt install code -y
