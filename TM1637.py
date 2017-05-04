#!/usr/bin/env python3

import subprocess
from time import time, sleep, localtime
import CHIP_IO.GPIO as GPIO

CLK = "GPIO5"
DIO = "GPIO6"

"""
      A
     ---
  F |   | B
     -G-
  E |   | C
     ---
      D

"""


class TM1637:
    I2C_COMM1 = 0x40
    I2C_COMM2 = 0xC0
    I2C_COMM3 = 0x80
    digit_to_segment = [
        0b0111111, # 0
        0b0000110, # 1
        0b1011011, # 2
        0b1001111, # 3
        0b1100110, # 4
        0b1101101, # 5
        0b1111101, # 6
        0b0000111, # 7
        0b1111111, # 8
        0b1101111, # 9
        0b1110111, # A
        0b1111100, # b
        0b0111001, # C
        0b1011110, # d
        0b1111001, # E
        0b1110001  # F
        ]

    def __init__(self, clk, dio):
        self.clk = clk
        self.dio = dio
        self.brightness = 0x0f
        print self.clk
        GPIO.setup(self.clk, GPIO.OUT)
        GPIO.setup(self.dio, GPIO.OUT)
        GPIO.direction(self.clk, GPIO.IN)
        GPIO.direction(self.dio, GPIO.IN)
        # GPIO.output(self.clk, GPIO.LOW)
        # GPIO.output(self.dio, GPIO.LOW)

    def bit_delay(self):
        return

    def set_segments(self, segments, pos=0):
        # Write COMM1
        self.start()
        self.write_byte(self.I2C_COMM1)
        self.stop()

        # Write COMM2 + first digit address
        self.start()
        self.write_byte(self.I2C_COMM2 + pos)

        for seg in segments:
            self.write_byte(seg)
        self.stop()

        # Write COMM3 + brightness
        self.start()
        self.write_byte(self.I2C_COMM3 + self.brightness)
        self.stop()

    def start(self):
        GPIO.direction(self.dio, GPIO.OUT)
        self.bit_delay()

    def stop(self):
        GPIO.direction(self.dio, GPIO.OUT)
        self.bit_delay()
        GPIO.direction(self.clk, GPIO.IN)
        self.bit_delay()
        GPIO.direction(self.dio, GPIO.IN)
        self.bit_delay()

    def write_byte(self, b):
      # 8 Data Bits
        for i in range(8):

            # CLK low
            GPIO.direction(self.clk, GPIO.OUT)
            self.bit_delay()

            GPIO.direction(self.dio, GPIO.IN if b & 1 else GPIO.OUT)

            self.bit_delay()

            GPIO.direction(self.clk, GPIO.IN)
            self.bit_delay()
            b >>= 1

        GPIO.direction(self.clk, GPIO.OUT)
        self.bit_delay()
        GPIO.direction(self.clk, GPIO.IN)
        self.bit_delay()
        GPIO.direction(self.clk, GPIO.OUT)
        self.bit_delay()

        return
