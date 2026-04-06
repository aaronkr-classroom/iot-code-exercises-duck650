#main.py

from device import SensorDevice, ActuatorDevice #파일 이름

sensor=SensorDevice("Temp Sensor")
actuator=ActuatorDevice("LED Controller")

sensor.connect()
actuator.connect()

print(sensor.status())
print(actuator.status())

temp=TemperatureSensor("Temp1")
light=LightSensor("Light1")

print("Temp: ", temp.read())
print("Light: ", light.read())