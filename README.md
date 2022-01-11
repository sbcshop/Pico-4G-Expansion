# Pico-4G-Expansion

<img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/img.png" />

## Setup Pico 4G Expansion
### Use 4G expansion module with pico 
   * Plug raspberry pi pico at the top of pico 4G expansion
   * In the folder you see two three python file :
     * Lcd1_14driver.py -> This file is of lcd display
     * EG25_4G.py -> This file contain the library of the module (including AT commands) , you need to add this file to pico .
     * main.py -> This is the main file you need to run
     
   * Inside the "main.py" file, you see three functions
     * To make a call, you need to uncomment this line Call = EG25_4G.call(Mobile_number,10) in main.py file
     * To make a message, you need to uncomment this line Message = EG25_4G.message(Mobile_number,Write_message) in main.py file
     * To turn on GPS, you need to uncomment this line Gps = EG25_4G.gps() in main.py file
   * You need to enter your mobile number in the code pico_2g_exp.py to make call and send the message

### Use Pico 4G Expansion without Pico

<img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/img1.jpg" />

First turn on the module by pressing the power button for three second, button is in the module as you see in the image. Then open any terminal which has AT command facility.
for example download XCTU software


    
    
  
