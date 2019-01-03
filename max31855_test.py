import time
import board
import busio
import digitalio
import adafruit_max31855
 
#spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
spi = busio.SPI(11, MOSI=10, MISO=9)
cs = digitalio.DigitalInOut(board.D5)
 
max31855 = adafruit_max31855.MAX31855(spi, cs)
while True:
    tempC = max31855.temperature
    tempF = tempC * 9 / 5 + 32
    print('Temperature: {} C {} F '.format(tempC, tempF))
    time.sleep(2.0)
