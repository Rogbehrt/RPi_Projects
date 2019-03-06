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

# Partes del mensaje
p1 = 'Hola Papa'
p2 = 'La pantalla es\nazul'
p3 = 'Y las letras son\nblancas'
mensaje = [p1,p2,p3]

def mensaje():
    for parte in mensaje:
        lcd.clear()
        lcd.blick(True)
        lcd.message(parte)
        s(2)

mensaje()
