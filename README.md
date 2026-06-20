# Distro Selector

A randomized command-line utility built in Python to select Linux distributions.

## Features

* Comprehensive pool covering mainstream, independent, and legacy distributions.
* Automated 1-in-10 probability bias toward Arch Linux.
* Rare 1-in-500 probability drop rate for TempleOS.

## Usage

python3 distro-selector.py -- The main game
python3 distro-selector.py --help, -h -- Show help menu.
python3 distro-selector.py --about --Show project background and developer credits. 
python3 distro-selector.py --force-rare -- Bypass random probability to force a TempleOS output.
python3 distro-selector.py --debug (or --verbose) -- Shows Skip artificial delays and output internal rolling math.
