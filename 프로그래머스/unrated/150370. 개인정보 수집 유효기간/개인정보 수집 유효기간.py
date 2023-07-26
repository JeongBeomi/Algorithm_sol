from datetime import date
def solution(today, terms, privacies):
    answer = []
    # 날짜비교를 위해 문자열 today를 date 객체로 변환
    date_today = date.fromisoformat(today.replace(".", "-"))
    terms_dict = {}
    # 유효기간을 쉽게 찾기 위해 딕셔너리로 변환
    for line in terms:
        name, term = line.split()
        terms_dict[name] = int(term)
    # 개인정보 리스트를 순회하며 파기해야하는지 확인
    for privacy_idx in range(len(privacies)):
        privacy_day, name = privacies[privacy_idx].split()
        # 개인정보저장 날짜에 유효기간을 더하기 위해서 연,월,일 int형으로 각각 저장
        privacy_y, privacy_m, privacy_d = map(int, privacy_day.split("."))
        # 유효기간 더해주기
        privacy_m += terms_dict[name] % 12
        privacy_y += terms_dict[name] // 12
        if privacy_m > 12:
            privacy_m = (privacy_m % 13) + 1
            privacy_y += 1
        # 비교를 위해서 date 객체로 변환
        date_privacy = date(privacy_y, privacy_m, privacy_d)
        print(date_today, date_privacy)
        if date_today >= date_privacy:
            answer.append(privacy_idx + 1)
    return answer