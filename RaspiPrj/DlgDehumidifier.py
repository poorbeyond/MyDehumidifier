# -*- coding: utf-8 -*-

"""
Module implementing DlgDehumidifier.
"""

import time
import multiprocessing
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer

from Ui_Dehumidifier import Ui_Dialog

import DehumidifierBLE

GREEN   = 0
RED     = 1
ORINGE  = 2
GRAY    = 3

e1 = multiprocessing.Event()
e2 = multiprocessing.Event()
queue = multiprocessing.Queue()
Device = []

def SetE1() :
    e1.set()

def SetE2() :
    e2.set()

def WaitE2() :
    e2.wait()
    e2.clear()

def GetDev() :
    return queue.get()

def ScanDev(e1, e2) :
    manager = DehumidifierBLE.AnyDeviceManager(adapter_name='hci0')
    while True :
        e1.wait()
        e1.clear()
        Device = []
        manager.start_discovery()
        manager.loop_start()
        time.sleep(10)
        manager.loop_stop()
        print('scan dev done...')
        for dev in manager.found_dev :
            Device.append(dev)
        queue.put(Device)
        manager.found_dev = []
        e2.set()
    

def SetLed(led,  color) :
    led.setText("")
    size = 20
    min_width = ("min-width: %dpx;") % size
    min_height = ("min-height: %dpx;") % size
    max_width = ("max-width: %dpx;") % (size)
    max_height = ("max-height: %dpx;") % (size)
    border_radius = ("border-radius: %dpx;") % (size/2)
    #border = ("border:1px solid black;")
    border = ("border:1px solid rgb(200,200,200);")
    background = "background-color: "
    if (color == GREEN) :
        background += "rgb(0,255,0)"
    elif (color == RED) :
        background += "rgb(237,28,36)"
    elif (color == ORINGE) :
        background += "rgb(255,127,39)"
    elif (color == GRAY) :
        background += "rgb(237,237,237)"

    SheetStyle = min_width + min_height + max_width + max_height + border_radius + border + background
    #SheetStyle = min_width + min_height + max_width + max_height + border_radius + background
    led.setStyleSheet(SheetStyle);

def UpdateLed(self,  data) :
    if (data & 0x1) == 0 :
        SetLed(self.LedH1,  GREEN)
    else :
        SetLed(self.LedH1,  GRAY)

    if (data & 0x2) == 0 :
        SetLed(self.LedH2,  GREEN)
    else :
        SetLed(self.LedH2,  GRAY)
    
    if (data & 0x4) == 0 :
        SetLed(self.LedH3,  GREEN)
    else :
        SetLed(self.LedH3,  GRAY)
    
    if (data & 0x8) == 0 :
        SetLed(self.LedH4,  GREEN)
    else :
        SetLed(self.LedH4,  GRAY)
    
    if (data & 0x10) == 0 :
        SetLed(self.LedM1,  ORINGE)
    else :
        SetLed(self.LedM1,  GRAY)
    
    if (data & 0x20) == 0 :
        SetLed(self.LedM2,  ORINGE)
    else :
        SetLed(self.LedM2,  GRAY)
    
    if (data & 0x40) == 0 :
        SetLed(self.LedM3,  ORINGE)
    else :
        SetLed(self.LedM3,  GRAY)
    
    if (data & 0x80) == 0 :
        SetLed(self.LedFull,  RED)
    else :
        SetLed(self.LedFull,  GRAY)
    
    # LED PWR 通过计算获得
    if (data != 255) :
        SetLed(self.LedPwr,  GREEN)
    else :
        SetLed(self.LedPwr,  GRAY)
    

class DlgDehumidifier(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    isConnect = 0
    wr_ch = None
    rd_ch = None
    p = None
    BleOP = None
    devices = []
    
    #def __init__(self, dev, parent=None):
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(DlgDehumidifier, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()       # 初始化定时器
        self.timer.timeout.connect(self.TimerEvent)
        
        SetLed(self.LedH1,  GRAY)
        SetLed(self.LedH2,  GRAY)
        SetLed(self.LedH3,  GRAY)
        SetLed(self.LedH4,  GRAY)
        SetLed(self.LedM1,  GRAY)
        SetLed(self.LedM2,  GRAY)
        SetLed(self.LedM3,  GRAY)
        SetLed(self.LedPwr,  GRAY)
        SetLed(self.LedFull,  GRAY)
        
        self.comboBox.setEnabled(False)
        self.BtnConnect.setEnabled(False)
        self.BtnDisconnect.setEnabled(False)
        self.groupOP.setEnabled(False)
        
        self.LabelStatus.hide()
        
            
    def TimerEvent(self) :
        self.BleOP.Write(bytearray(b'\xF9'))
        time.sleep(1)
        print('TimerEvent')
        data = self.BleOP.Read()
        print("%x, %x, %x" % (data[0],  data[1],  data[2]))
        print(int(data[0]))
        print(int("f9",  16))
        if ((data[0] == int("f9",  16)) and (data[2] == 0)) :
            UpdateLed(self, data[1])
        else :
            print('Read data Invalid')
        
    @pyqtSlot()
    def on_BtnSearch_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        
        print('searching...')
        self.comboBox.clear()
        SetE1()
        WaitE2()
        self.devices = GetDev()
        if len(self.devices) :
            for dev in self.devices :
                #self.comboBox.addItem(("%s  %s") % (dev.mac_address, dev.alias()))
                self.comboBox.addItem(("%s  ZQ-Dehumidifier") % (dev))
                #self.LabelStatus.setText(dev)
            self.BtnConnect.setEnabled(True)
            self.comboBox.setEnabled(True)
        else :
            self.BtnConnect.setEnabled(False)
            self.comboBox.setEnabled(False)
        
    
    @pyqtSlot()
    def on_BtnConnect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dev = self.devices[self.comboBox.currentIndex()]
        self.BleOP = DehumidifierBLE.BLE_OP(dev)
        self.BleOP.Connect()
        self.BtnDisconnect.setEnabled(True)
        self.groupOP.setEnabled(True)

        self.BtnConnect.setEnabled(False)
        self.BtnSearch.setEnabled(False)
        self.comboBox.setEnabled(False)
        
        # get Dehumidifier's status
        self.TimerEvent()
        self.timer.start(5 * 1000)
        
    
    @pyqtSlot()
    def on_BtnDisconnect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.BleOP.disConnect()
        self.BtnConnect.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.BtnSearch.setEnabled(True)

        self.BtnDisconnect.setEnabled(False)
        self.groupOP.setEnabled(False)
        self.timer.stop()
    
    @pyqtSlot()
    def on_BtnPwr_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.BleOP.Write(bytearray(b'\xF6\xF6\xF6'))
        self.TimerEvent()
        
    
    @pyqtSlot()
    def on_BtnMode_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.BleOP.Write(bytearray(b'\xF7\xF7\xF7'))
        self.TimerEvent()
        
    
    @pyqtSlot()
    def on_BtnHumidity_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.BleOP.Write(bytearray(b'\xF8\xF8\xF8'))
        self.TimerEvent()



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    p = multiprocessing.Process(target = ScanDev, args = (e1, e2))
    p.daemon = True
    p.start()

    app = QApplication(sys.argv)
    dlg = DlgDehumidifier()
    dlg.show()
    
    sys.exit(app.exec_())

