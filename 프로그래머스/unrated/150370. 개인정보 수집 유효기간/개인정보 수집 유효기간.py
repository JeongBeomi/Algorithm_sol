from datetime import date
def solution(today, terms, privacies):
    answer = []
    # 연,월,일 int형으로 각각 저장 후 today를 총 일수로 표현
    today_y, today_m, today_d = map(int, today.split("."))
    today_total = today_y * 12 * 28 + today_m * 28 + today_d
    # 유효기간을 쉽게 찾기 위해 딕셔너리로 변환
    terms_dict = {}
    for line in terms:
        name, term = line.split()
        terms_dict[name] = int(term)
    # 개인정보 리스트를 순회하며 파기해야하는지 확인
    for privacy_idx in range(len(privacies)):
        privacy_day, name = privacies[privacy_idx].split()
        # 연,월,일 int형으로 각각 저장
        privacy_y, privacy_m, privacy_d = map(int, privacy_day.split("."))
        # 유효기간 더한 개인정보 유효기간 총 일수 구하기
        privacy_total = privacy_y * 12 * 28 + privacy_m * 28 + privacy_d + terms_dict[name] * 28
        # 비교
        if today_total >= privacy_total:
            answer.append(privacy_idx + 1)
    return answer