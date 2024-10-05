from rpi_lcd import LCD
from time import sleep

lcd = LCD()
msg=input()

lcd.text(msg, 1)

