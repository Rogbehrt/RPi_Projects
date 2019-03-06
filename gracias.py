#!/usr/bin/python
import time
import Adafruit_CharLCD as LCD

# LCD settings
lcd_rs        = 12
lcd_en        = 06
lcd_d4        = 20
lcd_d5        = 26
lcd_d6        = 16
lcd_d7        = 19
lcd_backlight = 4
lcd_columns   = 16
lcd_rows      = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def s(t=0.33):
    return time.sleep(t)

lcd.blink(True)
lcd.message('Hola Papa')
s(2)
lcd.clear()
lcd.blink(True)
lcd.message('La pantalla es\nazul')
s(2)
lcd.clear()
lcd.blink(True)
lcd.message('Y las letras son\nblancas')
s(2)
lcd.clear()
lcd.blink(True)
lcd.message('Queria darte las\ngracias por')
s(2)
lcd.clear()
