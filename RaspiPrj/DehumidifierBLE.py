#!/usr/bin/env python
# coding=utf-8

import time
import threading
import gatt
#import sys
from bluepy.btle import UUID, Peripheral


class AnyDeviceManager(gatt.DeviceManager):
    found_dev = []
    def device_discovered(self, device):
        print("Discovered [%s] %s" % (device.mac_address, device.alias()))
        if (device.alias() == 'ZQ-Dehumidifier') and (device.mac_address not in self.found_dev) :
            self.found_dev.append(device.mac_address)
        
    def loop_start(self):
        self._thread = threading.Thread(target=self.run)
        self._thread.daemon = True
        self._thread.start()

    def loop_stop(self):
        self.stop()


class BLE_OP() :
    dev = None
    isConnect = 0
    wr_ch = None
    rd_ch = None
    p = None

    def __init__(self, device):
        self.dev = device
        
    def Connect(self) :
        if self.isConnect == 0 :
            wr_uuid = UUID('8d96b001-6001-64c2-0001-9acc4838521c')
            rd_uuid = UUID('8d96b002-6001-64c2-0001-9acc4838521c')
            
            self.p = Peripheral(self.dev, "random")
            self.wr_ch = self.p.getCharacteristics(uuid=wr_uuid)[0]
            self.rd_ch = self.p.getCharacteristics(uuid=rd_uuid)[0]
            self.isConnect = 1
            print("Connected")
        
    def disConnect(self) :
        if self.isConnect == 1 :
            self.p.disconnect()
            self.isConnect = 0
            self.wr_ch = None
            self.rd_ch = None
            self.p = None
            print("Disonnected")
        
    def Write(self,  data) :
        if self.isConnect == 1 :
            self.wr_ch.write(data)
        
    def Read(self) :
        if self.isConnect == 1 :
            return (bytearray)(self.rd_ch.read())
        else :
            return bytearray(b'\x00\x00\x00')
        
