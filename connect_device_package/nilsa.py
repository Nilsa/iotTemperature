#!/usr/bin/python
#! -*- coding: utf-8 -*-
# -----pamedir.py---------INENCO,invierno de 2017------Nilsa-Aien-Inca------
#------modificado de: AdafruitDHT.py-(Tony DiCola,Adafruit Industries,2014)-
# -----sensores: AM2302/DHT22----------------------------------------------- 
#------procesador: Raspberry pi 2B------------------------------------------
#------mide humedad y temperatura y guarda en un archivo a intervalos fijos-

# Importar librerias--------------------------------------------------------
import os
import sys
import time
import Adafruit_DHT
#os.system("mount -t vfat /dev/sda1 /media/pendrive")

# Abrir archivos--------------------------------------------------------------
fo = open ("losdatos", "a",1)
fo1 = open ("/media/pendrive/losdatos", "a",1)
archivo1 = open ("lapso_seg.txt", "r",1)

# Definir lapso entre lecturas------------------------------------------------
delay = int(archivo1.read())
# x = input ("lapso en segundos:  ")
# delay = x
# delay = 60

# Loop------------------------------------------------------------------------
while True:
  
    print "fecha:", time.strftime("%d.%m.%y")
    print "hora:", time.strftime("%H.%M.%S")
    fo.write(time.strftime("%d.%m.%y"))
    fo.write(",")
    fo.write(time.strftime("%H.%M.%S"))
    fo.write(",")  

    fo1.write(time.strftime("%d.%m.%y"))
    fo1.write(",")
    fo1.write(time.strftime("%H.%M.%S"))
    fo1.write(",")

    sensor = Adafruit_DHT.DHT22
    pin = 17
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    fo.write('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    fo1.write('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    

    print('Sensor 17:')
    print('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    fo.write(",")
   
    fo1.write(",")

    sensor = Adafruit_DHT.DHT22
    pin = 27
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    fo.write('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    fo1.write('{0:0.1f},{1:0.1f}'.format(temperature, humidity))    

    fo.write('\n')
    print('Sensor 27:')
    print('{0:0.1f},{1:0.1f}'.format(temperature, humidity))
    fo.write('\n')
    fo1.write('\n')
       
    sensor = Adafruit_DHT.DHT22
    pin = 22
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    print('Sensor 22')
    print('{0:0.1f},{0:0.1f}'.format(temperature,humidity))    

    time.sleep(delay)
