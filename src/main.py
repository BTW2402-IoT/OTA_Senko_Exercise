import sensor

s = sensor(Pin_SCL=22, Pin_SDA=23)
print(s.getAllData())
