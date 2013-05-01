#!/usr/bin/python

import usb
G9_VENDOR_ID = 0x046d
G9_PRODUCT_IDS = [0xc048, 0xc066]


def get_g9_handle():
    for bus in usb.busses():
        for device in bus.devices:
            if device.idVendor == G9_VENDOR_ID and \
                   device.idProduct in G9_PRODUCT_IDS:
                return device.open()
    return None


def g9_change_color(handle=None, red=None, green=None, blue=None):
    """ Change the color of an G9 leds
    g9: handle
    red: int between 0 and 255
    green: int between 0 and 255
    blue: int between 0 and 255
    """
    handle = handle or get_g9_handle()
    assert handle
    COMMAND = "\x10\x00\x80\x57"
    data = "%s%c%c%c" % (COMMAND, red, green, blue)
    REQUEST_TYPE = 0x34
    REQUEST = 0x09
    VALUE = 0x210
    INDEX = 0x01
    handle.controlMsg(REQUEST_TYPE, REQUEST, data,
                      VALUE, INDEX)


if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        g9_change_color(red=int(argv[1][:2], 16),
                        green=int(argv[1][2:4], 16),
                        blue=int(argv[1][4:6], 16))
    else:
        print 'Usage: g9led.py RRGGBB'
