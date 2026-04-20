# main.py

from lib.room_sensor import RoomSensor

# 객체 생성
sensor1 = RoomSensor("Living Room", 25.3, 60, 300)

# 값 출력
print("이름:", sensor1.name)
print("온도:", sensor1.temperature)
print("습도:", sensor1.humidity)
print("조도:", sensor1.light)