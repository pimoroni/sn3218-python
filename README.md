# SN3218

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/sn3218-python/test.yml?branch=main)](https://github.com/pimoroni/sn3218-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/sn3218-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/sn3218-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/sn3218.svg)](https://pypi.python.org/pypi/sn3218)
[![Python Versions](https://img.shields.io/pypi/pyversions/sn3218.svg)](https://pypi.python.org/pypi/sn3218)

# Pre-requisites

You must enable:

* i2c: `sudo raspi-config nonint do_i2c 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

# Installing

Stable library from PyPi:

* Just run `python3 -m pip install sn3218`

In most cases you'll need to run this in a virtual Python environment.

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/sn3218-python`
* `cd sn3218-python`
* `./install.sh --unstable`

