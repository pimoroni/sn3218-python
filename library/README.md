# SN3218

[![Build Status](https://shields.io/github/workflow/status/pimoroni/sn3218-python/Python%20Tests.svg)](https://github.com/pimoroni/sn3218-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/sn3218-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/sn3218-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/sn3218.svg)](https://pypi.python.org/pypi/sn3218)
[![Python Versions](https://img.shields.io/pypi/pyversions/sn3218.svg)](https://pypi.python.org/pypi/sn3218)

# Pre-requisites

You must enable:

* i2c: `sudo raspi-config nonint do_i2c 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

# Installing

Stable library from PyPi:

* Just run `pip3 install sn3218`

In some cases you may need to use `sudo` or install pip with: `sudo apt install python3-pip`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/sn3218-python`
* `cd sn3218-python`
* `sudo ./install.sh --unstable`


# Changelog
2.0.0
-----

* BREAKING: Port to class.
* Legacy support for module methods, auto-instantiates a class

1.2.7
-----

* Bugfix: Fix for Python 3.5

1.2.6
-----

* Initial commit to Raspbian apt repository

1.2.5
-----

* Initial commit to Raspbian apt repository

1.2.4
-----

* Added alternate warning/instructions for missing python3-smbus
* Code quality improvements

1.2.3
-----

* Print fix

1.2.2
-----

* Added i2c_bus_id detection for older Pi

1.2.1
-----

* Removed hard dependancy upon SMbus, added message at runtime

1.0.0
-----

* Initial release

