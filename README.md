# max31855_test
Raspberry Pi 3 Python3 MAX31855 test \
Pulled directly from https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/spi-sensors-devices \
## Hardware
Raspberry Pi 3 B+ \
[MAX31855 breakout](https://www.adafruit.com/product/269) 
## Pinout
Breakout Pin  | RPi3 GPIO |
------------- |-----------|
Vin | 5v            |
3Vo | No connect    |
GND | GND           |
DO  | Pin21, GPIO9  |
CS  | PIN29, GPIO5  |
CLK | PIN23, GPIO11 | 
## Install
`pip3 install adafruit-circuitpython-max31855` \
`pip3 install --upgrade adafruit_blinka` 
## Usage
`python3 max31855_test.py`
