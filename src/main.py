import sensor

s = sensor.Sensor(Pin_SCL=22, Pin_SDA=23, adress=0x77)
print(s.getAllData())

