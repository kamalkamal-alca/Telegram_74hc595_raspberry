import telepot  
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
from time import sleep      

GPIO.setmode(GPIO.BCM)
dataPin  = 24  # Pin for Data (GPIO 24)
latchPin = 23  # Pin for Latch (GPIO 23)
clockPin = 18  # Pin for Clock (GPIO 18)

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT)

# Variables
shift_data = 0b00000000  # Initial state of the shift register (all LEDs off)
previous_shift_data = 0b00000000

# Function to update shift register
def update_shift_register():
    global shift_data, previous_shift_data
    if shift_data != previous_shift_data:
        previous_shift_data = shift_data
        GPIO.output(latchPin, GPIO.LOW)
        shift_out(shift_data)
        GPIO.output(latchPin, GPIO.HIGH)

# Shift out data (similar to Arduino's shiftOut function)
def shift_out(data):
    for i in range(8):
        GPIO.output(clockPin, GPIO.LOW)
        GPIO.output(dataPin, (data >> (7 - i)) & 0x01)
        GPIO.output(clockPin, GPIO.HIGH)


def handle(msg):
    global shift_data
    
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received command:', command)
#=========================================================
    if command == '/led11':
        shift_data |= 0b00000001  
        bot.sendMessage(chat_id, "LED 1 ON")
        print(f"LED1 ON - Shift data: {bin(shift_data)}")   
    elif command == '/led10':
        shift_data &= 0b11111110  
        bot.sendMessage(chat_id, "LED 1 OFF")
        print(f"LED1 OFF - Shift data: {bin(shift_data)}")
#=========================================================   
    elif command == '/led21':
        shift_data |= 0b00000010  
        bot.sendMessage(chat_id, "LED 2 ON")
        print(f"LED2 ON - Shift data: {bin(shift_data)}")   
    elif command == '/led20':
        shift_data &= 0b11111101  
        bot.sendMessage(chat_id, "LED 2 OFF")
        print(f"LED2 OFF - Shift data: {bin(shift_data)}")
#=========================================================    
    elif command == '/led31':
        shift_data |= 0b00000100  
        bot.sendMessage(chat_id, "LED 3 ON")
        print(f"LED3 ON - Shift data: {bin(shift_data)}")  
    elif command == '/led30':
        shift_data &= 0b11111011  
        bot.sendMessage(chat_id, "LED 3 OFF")
        print(f"LED3 OFF - Shift data: {bin(shift_data)}")
#=========================================================    
    elif command == '/led41':
        shift_data |= 0b00001000 
        bot.sendMessage(chat_id, "LED 4 ON")
        print(f"LED4 ON - Shift data: {bin(shift_data)}")  
    elif command == '/led40':
        shift_data &= 0b11110111  
        bot.sendMessage(chat_id, "LED 4 OFF")
        print(f"LED4 OFF - Shift data: {bin(shift_data)}")
#=========================================================
    elif command == '/led51':
        shift_data |= 0b00010000 
        bot.sendMessage(chat_id, "LED 5 ON")
        print(f"LED5 ON - Shift data: {bin(shift_data)}")    
    elif command == '/led50':
        shift_data &= 0b11101111  
        bot.sendMessage(chat_id, "LED 5 OFF")
        print(f"LED5 OFF - Shift data: {bin(shift_data)}")
#=========================================================
    elif command == '/led61':
        shift_data |= 0b00100000 
        bot.sendMessage(chat_id, "LED 6 ON")
        print(f"LED6 ON - Shift data: {bin(shift_data)}")  
    elif command == '/led60':
        shift_data &= 0b11011111  
        bot.sendMessage(chat_id, "LED 6 OFF")
        print(f"LED6 OFF - Shift data: {bin(shift_data)}")
#=========================================================
    elif command == '/led71':
        shift_data |= 0b01000000 
        bot.sendMessage(chat_id, "LED 7 ON")
        print(f"LED7 ON - Shift data: {bin(shift_data)}")  
    elif command == '/led70':
        shift_data &= 0b10111111  
        bot.sendMessage(chat_id, "LED 7 OFF")
        print(f"LED7 OFF - Shift data: {bin(shift_data)}")
#=========================================================
    elif command == '/led81':
        shift_data |= 0b10000000 
        bot.sendMessage(chat_id, "LED 8 ON")
        print(f"LED8 ON - Shift data: {bin(shift_data)}")  
    elif command == '/led80':
        shift_data &= 0b01111111  
        bot.sendMessage(chat_id, "LED 8 OFF")
        print(f"LED8 OFF - Shift data: {bin(shift_data)}")
#=========================================================
    update_shift_register()

# Initialize the shift register to known state
update_shift_register()

# Bot setup
bot = telepot.Bot('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(bot.getMe())

MessageLoop(bot, handle).run_as_thread()
print('GPIOTEL 2.00 at your service...')

# Main loop - SIMPLE like Flask
try:
    while True:
        sleep(10)
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
