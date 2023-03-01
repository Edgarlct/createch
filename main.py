# from machine import Pin # importe dans le code la lib qui permet de gerer les Pin de sortie
# import utime # importe dans le code la lib qui permet de gerer le temps
#
# pinNumber = 17# declaration d'une variable pinNumber à 17
# led = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17
#                                    #et on prescise que c'est une pine de sortie de courant (OUT)
#
# while True:          # boucle infini
#     led.toggle()     # change l'etat de la led
#     utime.sleep(1)   # attendre 1 seconde
import json

# exo 6
# from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
# import time # importe dans le code la lib qui permet de gerer le temps
#
# pwm_led = PWM(Pin(17,mode=Pin.OUT)) # on prescise au programme que la pin 15 est une sortie de type PWN
# while True:
#     pwm_led.freq(1_000) # dont la frequence est de 1000 (default)
#     # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v
#     for i in range(0, 65535, 1000): # on incremente de 1000
#         pwm_led.duty_u16(i) # on lui donne la valeur i
#         time.sleep(0.01) # on attend 0.01 seconde
#     for i in range(65535, 0, -1000): # on decremente de 1000
#         pwm_led.duty_u16(i) # on lui donne la valeur i
#         time.sleep(0.01) # on attend 0.01 seconde


# exo 7
# we have button on pin 16 and led on pin 17
# if button is pressed, led is on
# if button is not pressed, led is off
# from machine import Pin # importe dans le code la lib qui permet de gerer les Pin de sortie
# import utime # importe dans le code la lib qui permet de gerer le temps
#
# pinNumber = 17# declaration d'une variable pinNumber à 17
# led = Pin(pinNumber, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17
# # et on prescise que c'est une pine de sortie de courant (OUT)
#
# button = Pin(16, mode=Pin.IN, pull=Pin.PULL_UP) # declaration d'une variable de type pin ici la 16
#
# while True: # boucle infini
#     if button.value() == 0: # si la valeur de la pin 16 est egale a 0
#         led.value(1) # alors la pin 17 est a 1
#     else: # sinon
#         led.value(0) # la pin 17 est a 0


# exo 8
# We have potentiometer on pin 26 and led on pin 17
# print value of potentiometer
# from machine import Pin, ADC,PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
# import utime # importe dans le code la lib qui permet de gerer le temps
#
# potentiometer = ADC(Pin(26)) # declaration d'une variable de type pin ici la 36
# led = PWM(Pin(17,mode=Pin.OUT)) # declaration d'une variable de type pin ici la 17
#
#
# while True: # boucle infini
#     print(potentiometer.read_u16()) # on affiche la valeur de la pin 36
#
#     led.duty_u16(potentiometer.read_u16()) # on affiche la valeur de la pin 36
#     # utime.sleep(0.1) # on attend 0.1 seconde
#

import urequests
import network

from Screen import Screen
from Wifi import Wifi

# wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
# wlan.active(True) # active le mode client wifi

# ssid = 'iPhone de Edgar'
# password = 'edouardlecon'
# wlan.connect(ssid, password) # connecte la raspi au réseau
#
# while not wlan.isconnected(): # tant que la raspi n'est pas connecté
#     pass # on fait rien
#
# url = "https://pokeapi.co/api/v2/pokemon/ditto"

# headers = {
#   'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOjE4MzgsInJpZ2h0cyI6WyJyZWFkOmFuc3dlcnMiLCJyZWFkOmJhZGdlcyIsInJlYWQ6cGF0aHMiLCJyZWFkOnNjZW5lcyIsInJlYWQ6c3BvdGxpZ2h0LXNjZW5lcyIsInJlYWQ6c3RlcHMiLCJyZWFkOnRhZy1wYXRoIiwicmVhZDp0YWctc2NlbmUiLCJyZWFkOnRhZy10aGVtZSIsInJlYWQ6dGFncyIsInJlYWQ6dGhlbWVzIiwicmVhZDp1c2VyLWJhZGdlIiwid3JpdGU6dXNlci1iYWRnZSIsInJlYWQ6dXNlci1pbmZvIiwid3JpdGU6dXNlci1pbmZvIiwicmVhZDp1c2VyLW5vdGlmcyIsIndyaXRlOnVzZXItbm90aWZzIiwicmVhZDp1c2VyLXBhdGgiLCJ3cml0ZTp1c2VyLXBhdGgiLCJyZWFkOnVzZXItc2NlbmUiLCJ3cml0ZTp1c2VyLXNjZW5lIiwicmVhZDp1c2VyLXRoZW1lIiwid3JpdGU6dXNlci10aGVtZSIsInJlYWQ6dXNlcnMiLCJ3cml0ZTp1c2VycyIsInJlYWQ6ZWxlbWVudHMiLCJyZWFkOmVsZW1lbnRzIiwicmVhZDpuZXdzIiwid3JpdGU6bmV3cyIsInJlYWQ6IG5ld3MtaW50ZXJhY3Rpb25zIiwid3JpdGU6IG5ld3MtaW50ZXJhY3Rpb25zIl0sImVtYWlsIjoiZWRvdWFyZC5uQGxpZmVhei5mciIsImlhdCI6MTY3NzU3NTU1MSwiZXhwIjoxNjgwMTY3NTUxfQ.QS81juiwpEKp7ZRmxYMt4SqgczmWRsw4GtWvELUeloA'
# }

# response = urequests.request("GET", url)
# print("oui")
# print(response.json())
# response.close()

# we want to get the pokemon type of ditto
# type = response.json()['types'][0]['type']['name']
# type = "grass"
# print(type)
#
# # we put the rgb led on pin 1, 2 and 3
# from machine import Pin, PWM
# import utime
#
# red = PWM(Pin(1, mode=Pin.OUT))
# green = PWM(Pin(2, mode=Pin.OUT))
# blue = PWM(Pin(3, mode=Pin.OUT))
# red.freq(1000)
# green.freq(1000)
# blue.freq(1000)
#
# # while True:
#     # we want to change the color of the led depending on the type of ditto
# print(type)
# print(type == "fire")
# if type == "fire":
#     print("fire")
#     red.duty_u16(65535)
#     green.duty_u16(0)
#     blue.duty_u16(0)
# elif type == "water":
#     print("water")
#     red.duty_u16(0)
#     green.duty_u16(0)
#     blue.duty_u16(65535)
# elif type == "grass":
#     print("grass")
#     red.duty_u16(0)
#     green.duty_u16(65535)
#     blue.duty_u16(0)
#
#

# wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
# wlan.active(True) # active le mode client wifi
#
# ssid = 'IIM_Private'
# password = 'Creatvive_Lab_2023'
# wlan.connect(ssid, password) # connecte la raspi au réseau
#
# while not wlan.isconnected(): # tant que la raspi n'est pas connecté
#     pass # on fait rien
#
# url = "https://staging.api.everydayheroes.fr/api/v2/app/users/me/clark/tracking"
#
# headers = {
#   'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZFVzZXIiOjE4MzgsInJpZ2h0cyI6WyJyZWFkOmFuc3dlcnMiLCJyZWFkOmJhZGdlcyIsInJlYWQ6cGF0aHMiLCJyZWFkOnNjZW5lcyIsInJlYWQ6c3BvdGxpZ2h0LXNjZW5lcyIsInJlYWQ6c3RlcHMiLCJyZWFkOnRhZy1wYXRoIiwicmVhZDp0YWctc2NlbmUiLCJyZWFkOnRhZy10aGVtZSIsInJlYWQ6dGFncyIsInJlYWQ6dGhlbWVzIiwicmVhZDp1c2VyLWJhZGdlIiwid3JpdGU6dXNlci1iYWRnZSIsInJlYWQ6dXNlci1pbmZvIiwid3JpdGU6dXNlci1pbmZvIiwicmVhZDp1c2VyLW5vdGlmcyIsIndyaXRlOnVzZXItbm90aWZzIiwicmVhZDp1c2VyLXBhdGgiLCJ3cml0ZTp1c2VyLXBhdGgiLCJyZWFkOnVzZXItc2NlbmUiLCJ3cml0ZTp1c2VyLXNjZW5lIiwicmVhZDp1c2VyLXRoZW1lIiwid3JpdGU6dXNlci10aGVtZSIsInJlYWQ6dXNlcnMiLCJ3cml0ZTp1c2VycyIsInJlYWQ6ZWxlbWVudHMiLCJyZWFkOmVsZW1lbnRzIiwicmVhZDpuZXdzIiwid3JpdGU6bmV3cyIsInJlYWQ6IG5ld3MtaW50ZXJhY3Rpb25zIiwid3JpdGU6IG5ld3MtaW50ZXJhY3Rpb25zIl0sImVtYWlsIjoiZWRvdWFyZC5uQGxpZmVhei5mciIsImlhdCI6MTY3NzU3NTU1MSwiZXhwIjoxNjgwMTY3NTUxfQ.QS81juiwpEKp7ZRmxYMt4SqgczmWRsw4GtWvELUeloA',
#   'Content-Type': 'application/json'
# }
#
# # try catch
# try:
#     response = urequests.request("GET", url, headers=headers)
#     response.encoding = 'utf-8'
#     print(response.content)
#     print(response.headers)
#     print(response.status_code)
#     response.close()
# except (OSError, ValueError) as e:
#     print("error")
#     print(e)


# we want to play music with the buzzer
# the buzzer is on pin 2
#
# from machine import Pin, PWM
# import utime
#
# buzzer = PWM(Pin(2, mode=Pin.OUT))
# buzzer.freq(1000)
#
# tones = {
#     "C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93, "G2": 98, "GS2": 104, "A2": 110,
#     "AS2": 117, "B2": 123, "C3": 131, "CS3": 139, "D3": 147, "DS3": 156, "E3": 165, "F3": 175, "FS3": 185,
#     "G3": 196, "GS3": 208, "A3": 220, "AS3": 233, "B3": 247, "C4": 262, "CS4": 277, "D4": 294, "DS4": 311,
#     "E4": 330, "F4": 349, "FS4": 370, "G4": 392, "GS4": 415, "A4": 440, "AS4": 466, "B4": 494, "C5": 523,
#     "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740, "G5": 784, "GS5": 831, "A5": 880,
#     "AS5": 932, "B5": 988, "C6": 1047, "CS6": 1109, "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397,
#     "FS6": 1480, "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976, "C7": 2093, "CS7": 2217,
#     "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960, "G7": 3136, "GS7": 3322, "A7": 3520,
#     "AS7": 3729, "B7": 3951, "C8": 4186
# }
#
# song = []
#
# happy_birthday = [
#     "G4", "G4", "A4", "G4", "C5", "B4",
#     "G4", "G4", "A4", "G4", "D5", "C5",
#     "G4", "G4", "G5", "E5", "C5", "B4", "A4",
#     "F5", "F5", "E5", "C5", "D5", "C5", "G4", "G4", "A4", "G4", "C5", "B4",
#     "G4", "G4", "A4", "G4", "D5", "C5",
#     "G4", "G4", "G5", "E5", "C5", "B4", "A4",
#     "F5", "F5", "E5", "C5", "D5", "C5"
# ]
#
# marseillaise = ["G4", "G4", "G4", "D4", "G4", "C5", "G4", "G4", "G4", "D4", "G4", "D5", "G4", "G4", "G4", "G5", "E5",
#                 "D5", "C5", "B4", "C5", "G4", "E5", "C5", "G4", "G4", "G4", "D4", "G4", "C5", "G4", "G4", "G4", "D4",
#                 "G4", "D5", "G4", "G4", "G4", "G5", "E5", "D5", "C5", "B4", "C5", "G4", "E5", "C5", "G4", "D5", "E5",
#                 "F5", "E5", "D5", "C5", "D5", "E5", "F5", "E5", "D5", "C5", "D5", "E5", "D5", "C5", "B4", "C5", "D5",
#                 "E5", "F5", "G5", "C5", "G4", "D5", "E5", "F5", "E5", "D5", "C5", "D5", "E5", "F5", "E5", "D5", "C5",
#                 "D5", "E5", "D5", "C5", "B4", "C5", "D5", "E5", "F5", "G5", "C5"]
#
#
# def playtone(frequency):
#     buzzer.duty_u16(1000)
#     buzzer.freq(frequency)
#
#
# def bequiet():
#     buzzer.duty_u16(0)
#
#
# def playsong(mysong):
#     for i in range(len(mysong)):
#         if (mysong[i] == "P"):
#             bequiet()
#         else:
#             playtone(tones[mysong[i]])
#         utime.sleep(0.3)
#     bequiet()
#
#
# playsong(marseillaise)

# we want to display a message on the OLED
# the OLED is on I2C bus 0, address 0x3c

# from machine import Pin, I2C
# import ssd1306
# import utime
#
# i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
# oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#
# oled.fill(0)
# # letter width is 6 pixels
# text = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor"
#
# screen_width = oled.width
# screen_height = oled.height
# letter_width = 9
# letter_height = 8
# text_width = len(text) * letter_width
# print(screen_width, screen_height, text_width)
# for i in range(text_width - screen_width):
#     oled.fill(0)
#     oled.text(text[i // letter_width:], 0, 0)
#     oled.show()
#     utime.sleep(0.001)

screen = Screen()
# wifi = Wifi("IIM_Private", "Creatvive_Lab_2023", screen)
wifi = Wifi("iPhone de Edgar", "edouardlecon", screen)

wifi.connect()




