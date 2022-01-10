import machine
import os
import utime
import time
import Lcd1_14driver
import EG25_4G

LCD = Lcd1_14driver.Lcd1_14()#driver of lcd display

def infoDevice():
        LCD.fill(LCD.black) 
        LCD.hline(10,10,220,LCD.white)
        LCD.hline(10,125,220,LCD.white)
        LCD.vline(10,10,115,LCD.white)
        LCD.vline(230,10,115,LCD.white)       
        
        LCD.text("SB-COMPONENTS",70,40,LCD.white)
        LCD.text("PICO 4G",70,60,LCD.white)
        LCD.text("EXPANSION",70,80,LCD.white)  
        LCD.lcd_show()
        time.sleep(2)
        LCD.fill(LCD.black)
        LCD.text("WAITING.....",70,40,LCD.white)
        LCD.lcd_show()
        x = 0
        for y in range(0,1):
                x += 4
                LCD.text(".",125+x,40,LCD.white)
                LCD.lcd_show()
                time.sleep(1)

infoDevice()

Mobile_number = "write_your_mobile_number_here" #write your phone number here 
Write_message = "Hello World !!!!" #write message you need to send

Message = EG25_4G.message(Mobile_number,Write_message) #send the message

#Call = EG25_4G.call(Mobile_number,60) # uncomment this to make call 60 means duration of call(you can change according to you)

#Gps = EG25_4G.gps() #uncomment this to use gps
 