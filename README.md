# TM1637 Driver

This is a Python Driver for the TM1637 display, such as the following: [TM1637](https://www.amazon.com/HiLetgo-Digital-Segment-Display-Arduino/dp/B01DKISMXK/ref=sr_1_2?ie=UTF8&qid=1493866378&sr=8-2&keywords=TM1637). It is specifically design for the [CHIP](getchip.com) by Next Thing Co.

## Installation

This driver requires the [CHIP_IO](https://github.com/xtacocorex/CHIP_IO) python package written by xtacocorex.

For now to install simply add the TM1637.py file to your project and import as needed. I may setup a python package later depending on if someone asks or not.

## Usage

Here is an example implementation of this driver:

```
import TM1637

//Import driver and specify GPIO pins used for clock and data (respectively)
tm = TM1637.TM1637("XIO-P6","XIO-P7")
digit = tm.digit_to_segment[1]
tm.set_segment([digit,0,0,0])


```
