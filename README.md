# TM1637 Driver

This is a Python Driver for the TM1637 display, such as the following: [TM1637](https://www.amazon.com/HiLetgo-Digital-Segment-Display-Arduino/dp/B01DKISMXK/ref=sr_1_2?ie=UTF8&qid=1493866378&sr=8-2&keywords=TM1637). It is specifically design for the [CHIP](getchip.com) by Next Thing Co.

## Installation

This driver requires the [CHIP_IO](https://github.com/xtacocorex/CHIP_IO) python package written by xtacocorex. *You must install this before the driver will work.*

For now to install simply add the TM1637.py file to your project and import as needed. I may setup a python package later depending on if someone asks or not.

## Functions

### set_segments(segments)

This function accepts an array of encoded segments. In order to convert a digit or digits to work with this function, you must use `digit_to_segment`.

### digit_to_segment

Not actually a function, but a Python list, where index values match the digit needed. These are the segments available from the driver:

```
[
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
```

So calling `digit_to_segment[10]` would return the code for the letter A and so on.

### clear()

Simple function to clear all previous data the screen may have been displaying. I've noticed that at least on my model, it seems to store previous data, so setting only the first segment after restoring power causes the device to display the new first segment and the older three segments together.

## Usage

Here is an example implementation of this driver:

```
import TM1637

# Import driver and specify GPIO pins used for clock and data (respectively)
tm = TM1637.TM1637("XIO-P6","XIO-P7")

# Convert your digit to a segment code
digit = tm.digit_to_segment[1]

# Clear any previous data the display may have
tm.clear()

# Set display segments (they run from Left to Right)
tm.set_segment([digit])


```
