# ==================================
# Modern Smart Farm System (Tomato)
# ==================================

# ----- 토마토 최적 생육 기준 -----
OPTIMAL = {
    "temperature": 24,    # ℃
    "humidity": 60,       # %
    "co2": 800,           # ppm
    "light": 20000,       # lux
    "soil": 70            # %
}

TOLERANCE = {
    "temperature": 6,
    "humidity": 15,
    "co2": 400,
    "light": 8000,
    "soil": 15
}


def score(value, optimal, tolerance):
    diff = abs(value - optimal)
    return max(0, 25 * (1 - diff / tolerance))


# ----- 환경 입력 -----
print("토마토 스마트팜 환경 시뮬레이션")
print("환경 값을 입력하세요\n")

env = {}
env["temperature"] = float(input("온도 (℃): "))
env["humidity"] = float(input("습도 (%): "))
env["co2"] = float(input("CO₂ 농도 (ppm): "))
env["light"] = float(input("조도 (lux): "))
env["soil"] = float(input("토양 수분 (%): "))


# ----- 성장 적합도 계산 -----
total_score = 0
for key in OPTIMAL:
    total_score += score(env[key], OPTIMAL[key], TOLERANCE[key])

growth_rate = total_score / 10  # %


# ----- 스마트팜 자동 제어 판단 -----
control = []

if env["temperature"] < OPTIMAL["temperature"]:
    control.append("히터 가동")
elif env["temperature"] > OPTIMAL["temperature"]:
    control.append("냉각 시스템 가동")

if env["humidity"] < OPTIMAL["humidity"]:
    control.append("가습기 가동")
elif env["humidity"] > OPTIMAL["humidity"]:
    control.append("환기 시스템 가동")

if env["co2"] < OPTIMAL["co2"]:
    control.append("CO₂ 공급")
elif env["co2"] > OPTIMAL["co2"]:
    control.append("환기 강화")

if env["light"] < OPTIMAL["light"]:
    control.append("인공 조명 강화")

if env["soil"] < OPTIMAL["soil"]:
    control.append("관수 시스템 가동")


# ----- 결과 출력 -----
print("\n토마토 생육 분석 결과")
print(f"성장 적합도 점수: {total_score:.2f} / 125")
print(f"예상 성장률: {growth_rate:.2f} %")

if growth_rate >= 7:
    print("판정: 최적 생육 가능")
elif growth_rate >= 4:
    print("판정: 생육 가능하나 조건 보정 필요")
else:
    print("판정: 생육 부적합")

print("\n스마트팜 자동 제어 제안")
if control:
    for c in control:
        print(" -", c)
else:
    print(" - 모든 조건이 토마토 최적 범위에 있음")