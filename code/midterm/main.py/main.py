# main.py

from lib.room_sensor import RoomSensor

# 센서 객체 3개 생성
sensor1 = RoomSensor("Kitchen", 31, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 300)
sensor3 = RoomSensor("Balcony", 18, 35, 150)

# 리스트에 저장
sensors = [sensor1, sensor2, sensor3]

# 상태 카운트 변수
comfortable_count = 0
normal_count = 0
warning_count = 0

# 반복문
for sensor in sensors:
    sensor.show_info()

    comfort = sensor.comfort_level()
    light = sensor.light_status()

    print(f"Comfort Level: {comfort}")
    print(f"Light Status: {light}")
    print()  # 줄 띄우기

    # 상태 카운트
    if comfort == "Comfortable":
        comfortable_count += 1
    elif comfort == "Normal":
        normal_count += 1
    elif comfort == "Warning":
        warning_count += 1

# 결과 출력
print("=== Summary ===")
print(f"Comfortable: {comfortable_count}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")
