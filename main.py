#!/usr/bin/env python3
import os
import pyudev
import zenity
import usb.core

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem="usb")
for device in iter(monitor.poll, None):
    if device.action == "add":
        print("{} connected".format(device))
        if usb.core.find(idVendor=0x0781, idProduct=0x558A) is not None:
            res, _ = zenity.show(zenity.notification, text="Finch Connected")
            os.system("xset dpms force on")
    if device.action == "remove":
        print("{} disconnected".format(device))
        while usb.core.find(idVendor=0x0781, idProduct=0x558A) is None:
            res, _ = zenity.show(zenity.notification, text="Finch Disconnected")
            os.system("xset dpms force off")
            # os.system("sudo loginctl lock-sessions")

