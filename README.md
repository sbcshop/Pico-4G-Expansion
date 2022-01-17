# Pico-4G-Expansion

<img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/image/img.png" />

## Setup Pico 4G Expansion
### Use 4G expansion module with pico 
   * Plug raspberry pi pico at the top of pico 4G expansion
   * In the folder you see 3 python files:
     * Lcd1_14driver.py -> This file contain library of lcd display
     * EG25_4G.py -> This file contain the library of the module (including AT commands) , you need to add this file to pico .
     * main.py -> This is the main file you need to run
     
   * Inside the "main.py" file, you see three functions
     * To make a call, you need to uncomment this line Call = EG25_4G.call(Mobile_number,10) in main.py file
     * To make a message, you need to uncomment this line Message = EG25_4G.message(Mobile_number,Write_message) 
       in main.py file
     * To turn on GPS, you need to uncomment this line Gps = EG25_4G.gps() in main.py file
   * You need to enter your mobile number in the code main.py to make call and send the message

### Use Pico 4G Expansion without Pico

   <img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/image/img1.jpg" />

   First turn on the module by pressing the power button for three second ( with pico you don,t need to press this button because module is turn on with the help of code) button    is in the module as you see in the image. Then open any terminal which has AT command facility.
   for example download "AT Command Tester" software,as shown in figure

   <img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/image/img3.jpg" />


   Open port configuration,select COM port and set baud rate (115200 is default). After that click on connect icon
   <img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/image/img4.JPG" />
   
   There are numerous features in "AT command tester" software as per the image below
   
   <img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/image/img_5.JPG" />
   
   For example: If you want to call, go to voice call option, then write your mobile number in blank box, as shown image below:
   
   <img src = "https://github.com/sbcshop/Pico-4G-Expansion/blob/main/image/img6.JPG" />

### Link of the AT Command Tester software
https://m2msupport.net/m2msupport/download-at-command-tester/

### <a href="https://learn.sb-components.co.uk/Pico-4g-expansion" > Pico 4G Expansion Wiki Portal </a>

     
   

    
    
  
