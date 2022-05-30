from ssl import HAS_SNI
import BME280
import esp32
from machine import Pin, SoftI2C

class Sensor:
    
    def __init__(self, Pin_SCL=22 ,Pin_SDA=21, adress=0x77):
        """BME280 class.

        Args:
            Pin_SCL (int): SCL Pin
            Pin_SDA (int): SDA Pin
            adress (hex):  alternativ BME280 senor Adress
        """
        self.i2c = SoftI2C(scl=Pin(Pin_SCL), sda=Pin(Pin_SDA), freq=10000)
        self.bme = BME280.BME280(adress=adress, i2c=self.i2c)

    def getTemp(self):
        t = float(self.bme.read_temperature()) / 100
        return t

    def getHumi(self):
        h = float(self.bme.read_humidity()) / 1024
        return h

    def getPres(self):
        p = float(self.bme.read_pressure()) / 100
        return p

    def getAllData(self):
        t = float(self.bme.read_temperature()) / 100
        p = float(self.bme.read_pressure()) / 100
        h = float(self.bme.read_humidity()) / 1024
        if isinstance(t, float) and isinstance(h, float) and isinstance(p, float):
            msg = (b'{0:3.1f},{1:3.1f},{2:3.1f}'.format(t,h,p))
        
        return msg

    def getHal():
        hs = esp32.hall_sensor()
        return HAS_SNI

