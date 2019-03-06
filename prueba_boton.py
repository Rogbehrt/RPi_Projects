#!/usr/bin/python
import time
import Adafruit_CharLCD as LCD
from gpiozero import Button

button = Button(2)

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
p4 = 'Gracias por los\npines.'
gracias = [p1,p2,p3]
def main():
    def mensaje(m):
        lcd.clear()
        lcd.blink(True)
        lcd.message(m)
        s(2)
        lcd.blink(False)
    for parte in gracias:
        mensaje(parte)
    lcd.clear()
    lcd.blink(False)
    # lcd.show_cursor(True)
    mensaje(p4)
    s(2)
    # lcd.show_cursor(False)
    lcd.clear()
    message = '=D'
    lcd.message(message)
    s(2)
    for i in range(lcd_columns-len(message)):
        s(0.2)
        lcd.move_right()
    for i in range(lcd_columns-len(message)):
        s(0.2)
        lcd.move_left()
    lcd.clear()
    message = '\n=D'
    lcd.message(message)
    for i in range(lcd_columns-len(message)):
        s(0.2)
        lcd.move_right()
    for i in range(lcd_columns-len(message)):
        s(0.2)
        lcd.move_left()
    s(2)
    lcd.clear()

presionado = button.is_pressed()
while True:
    if presionado:
        lcd.message('Hola')
        s(1)
        lcd.clear()
