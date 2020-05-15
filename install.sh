#!/bin/bash

set -e

export PYENV_VERSION=$1

command -v brew >/dev/null 2>&1 || \
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

export PATH=/usr/local/bin:$PATH

brew update

command -v pyenv >/dev/null 2>&1 || \
    brew install pyenv pyenv-virtualenv

pyenv install -s ${PYENV_VERSION}
profile="$HOME/.$(basename $SHELL)rc"
echo 'eval "$(pyenv init -)"' >> $profile
echo 'eval "$(pyenv virtualenv-init -)"' >> $profile
source $profile
pyenv virtualenv ${PYENV_VERSION} game-${PYENV_VERSION} || true
pyenv local game-${PYENV_VERSION}
