class SayDays:
    def __init__(self, year, month, day):
        self.y = year
        self.m = month
        self.d = day
        # 해당 연도가 윤년인지 판별 (4로 나누어 떨어지고 100으로 안 나누어지거나, 400으로 나누어 떨어짐)
        self.is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        # 월별 일수 리스트 (index 0은 더미)
        self.month_days = [0, 31, 29 if self.is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def days(self):
        """1월 1일 기준 현재 날짜가 몇 번째 날인지 계산"""
        total = sum(self.month_days[:self.m]) + self.d
        return total

    def days_left(self):
        """12월 31일 기준 남은 일수 계산"""
        year_total = 366 if self.is_leap else 365
        return year_total - self.days()

    def weekday(self):
        """Zeller의 공식을 이용한 요일 숫자 계산 (0:토, 1:일, ... 6:금)"""
        y, m, d = self.y, self.m, self.d
        
        # Zeller 공식에서 1, 2월은 전년도 13, 14월로 계산함
        if m < 3:
            m += 12
            y -= 1
        
        K = y % 100          # 연도의 마지막 두 자리
        J = y // 100         # 세기 (앞의 두 자리)
        
        # Zeller's congruence 공식
        h = (d + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
        return h

    def weekday_name(self):
        """숫자 요일을 한글 이름으로 변환"""
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]


while True:
    try:
        user_input = input("날짜를 입력하세요 (예: 2026 4 6, 종료는 q): ")
        if user_input.lower() == 'q':
            break
            
        # 입력받은 값을 공백 기준으로 분리하여 정수로 변환
        y, m, d = map(int, user_input.split())
        
        # 오브젝트 생성
        sd = SayDays(y, m, d)
        
        # 결과 출력
        print(f"[{y}년 {m}월 {d}일 결과]")
        print(f"- 1월 1일 기준: {sd.days()}째 날")
        print(f"- 올해 남은 일수: {sd.days_left()}일")
        print(f"- 요일 숫자(0:토): {sd.weekday()}")
        print(f"- 요일 이름: {sd.weekday_name()}")
        print("-" * 30)
        
    except ValueError:
        print("올바른 형식으로 입력해주세요 (연 월 일).")
