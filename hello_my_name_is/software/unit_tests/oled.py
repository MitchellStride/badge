# https://pypi.org/project/oled-text/

# Display Image & text on I2C driven ssd1306 OLED display
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import framebuf

#N096-2864KSWEG01-H30
WIDTH = 128 # oled display width
HEIGHT = 64 # oled display height

oled_rst = machine.Pin(15, machine.Pin.OUT)
oled_rst.low()
utime.sleep(0.1)
oled_rst.high()
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))

#i2c = I2C(0) # Init I2C using I2C0 defaults,
#SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
print("I2C Address : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c)) # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Init oled display

# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

buffer2 = bytearray(b'0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xe0, 0x7f, 0xf0, 0x7e, 0x38, 0x00, 0x07, 0xf8, 0x3f, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc0, 0x7f, 0xe0, 0x3e, 0x38, 0x00, 0x07, 0xc0, 0x0f, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc0, 0x3f, 0xe0, 0x3e, 0x38, 0x00, 0x07, 0x80, 0x07, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc0, 0x3f, 0xc0, 0x3e, 0x3f, 0xe1, 0xff, 0x03, 0xc7, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc2, 0x3f, 0xc4, 0x3e, 0x3f, 0xe1, 0xff, 0x0f, 0xf7, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc2, 0x1f, 0x84, 0x3e, 0x3f, 0xe1, 0xfe, 0x1f, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc2, 0x1f, 0x8c, 0x3e, 0x3f, 0xe1, 0xfe, 0x1f, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0x1f, 0x8c, 0x3e, 0x3f, 0xe1, 0xfe, 0x1f, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0x0f, 0x0c, 0x3e, 0x3f, 0xe1, 0xfc, 0x1f, 0xff, 0x00, 0x00, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0x0f, 0x1c, 0x3e, 0x3f, 0xe1, 0xfc, 0x1f, 0xff, 0x00, 0x00, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0x87, 0x1c, 0x3e, 0x3f, 0xe1, 0xfc, 0x1f, 0xff, 0x00, 0x00, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0x86, 0x1c, 0x3e, 0x3f, 0xe1, 0xfc, 0x1f, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xc6, 0x3c, 0x3e, 0x3f, 0xe1, 0xfe, 0x1f, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xc0, 0x3c, 0x3e, 0x3f, 0xe1, 0xfe, 0x1f, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xc0, 0x3c, 0x3e, 0x3f, 0xe1, 0xfe, 0x1f, 0xff, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xe0, 0x7c, 0x3e, 0x3f, 0xe1, 0xfe, 0x0f, 0xf7, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xe0, 0x7c, 0x3e, 0x3f, 0xe1, 0xff, 0x07, 0xc7, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xe0, 0x7c, 0x3e, 0x3f, 0xe1, 0xff, 0x80, 0x07, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xf0, 0xfc, 0x3e, 0x3f, 0xe1, 0xff, 0xc0, 0x0f, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xc3, 0xf0, 0xfc, 0x3e, 0x3f, 0xe1, 0xff, 0xf0, 0x3f, 0x0f, 0xf0, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xc0, 0xf0, 0x00, 0x0c, 0x00, 0xff, 0x8f, 0x80, 0x1f, 0xfc, 0x00, 0x7f, 0xff, 0xff
0xff, 0xff, 0x00, 0x30, 0x00, 0x0c, 0x00, 0x3f, 0x8f, 0x80, 0x03, 0xf8, 0x00, 0x7f, 0xff, 0xff
0xff, 0xfe, 0x00, 0x30, 0x00, 0x0c, 0x00, 0x1f, 0x8f, 0x80, 0x01, 0xf8, 0x00, 0x7f, 0xff, 0xff
0xff, 0xfe, 0x1f, 0x3f, 0xc3, 0xfc, 0x3e, 0x0f, 0x8f, 0x87, 0xc0, 0xf8, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfe, 0x1f, 0xff, 0xc3, 0xfc, 0x3f, 0x0f, 0x8f, 0x87, 0xf0, 0x78, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfc, 0x3f, 0xff, 0xc3, 0xfc, 0x3f, 0x0f, 0x8f, 0x87, 0xf8, 0x78, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfe, 0x1f, 0xff, 0xc3, 0xfc, 0x3f, 0x0f, 0x8f, 0x87, 0xf8, 0x78, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfe, 0x07, 0xff, 0xc3, 0xfc, 0x3f, 0x0f, 0x8f, 0x87, 0xfc, 0x38, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfe, 0x01, 0xff, 0xc3, 0xfc, 0x3e, 0x1f, 0x8f, 0x87, 0xfc, 0x38, 0x00, 0xff, 0xff, 0xff
0xff, 0xff, 0x00, 0x7f, 0xc3, 0xfc, 0x00, 0x1f, 0x8f, 0x87, 0xfc, 0x38, 0x00, 0xff, 0xff, 0xff
0xff, 0xff, 0xc0, 0x3f, 0xc3, 0xfc, 0x00, 0x7f, 0x8f, 0x87, 0xfc, 0x38, 0x00, 0xff, 0xff, 0xff
0xff, 0xff, 0xf0, 0x3f, 0xc3, 0xfc, 0x00, 0x7f, 0x8f, 0x87, 0xfc, 0x38, 0x7f, 0xff, 0xff, 0xff
0xff, 0xff, 0xfc, 0x1f, 0xc3, 0xfc, 0x38, 0x3f, 0x8f, 0x87, 0xfc, 0x38, 0x7f, 0xff, 0xff, 0xff
0xff, 0xff, 0xfe, 0x1f, 0xc3, 0xfc, 0x3c, 0x1f, 0x8f, 0x87, 0xf8, 0x78, 0x7f, 0xff, 0xff, 0xff
0xff, 0xff, 0xfe, 0x1f, 0xc3, 0xfc, 0x3e, 0x1f, 0x8f, 0x87, 0xf8, 0x78, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfd, 0xfe, 0x1f, 0xc3, 0xfc, 0x3e, 0x0f, 0x8f, 0x87, 0xf0, 0x78, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfc, 0x7c, 0x3f, 0xc3, 0xfc, 0x3f, 0x0f, 0x8f, 0x87, 0xc0, 0xf8, 0x7f, 0xff, 0xff, 0xff
0xff, 0xfc, 0x00, 0x3f, 0xc3, 0xfc, 0x3f, 0x0f, 0x8f, 0x80, 0x01, 0xf8, 0x00, 0x7f, 0xff, 0xff
0xff, 0xfe, 0x00, 0x7f, 0xc3, 0xfc, 0x3f, 0x87, 0x8f, 0x80, 0x03, 0xf8, 0x00, 0x7f, 0xff, 0xff
0xff, 0xff, 0x81, 0xff, 0xc3, 0xfc, 0x3f, 0x87, 0x8f, 0x80, 0x1f, 0xfc, 0x00, 0x7f, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff')

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# Clear the oled display in case it has junk on it.
oled.fill(0)

# Blit the image from the framebuffer to the oled display
oled.blit(fb, 96, 0)

# Add some text
oled.text("Raspberry Pi",5,5)
oled.text("Pico",5,15)
oled.text("#badgelife", 25, 35)
oled.text("Mitch Stride", 15, 55)

# Finally update
oled.show()