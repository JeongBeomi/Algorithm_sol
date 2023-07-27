def solution(fees, records):
    answer = []
    check_dict = dict()
    utime_dict = dict()
    for record in records:
        record_t, record_n, record_s = record.split()
        i_time = check_dict.get(record_n)
        # check_dict 존재하지않으면 입차
        if i_time == None:
            check_dict[record_n] = record_t
            continue
        # check_dict 존재하면 출차 이용시간 계산후 삭제처리
        i_h, i_m = map(int, i_time.split(":"))
        o_h, o_m = map(int, record_t.split(":"))
        u_time = (o_h - i_h) * 60 + (o_m - i_m)
        del check_dict[record_n]
        # 계산한 이용시간을 utime_dict에 추가
        if utime_dict.get(record_n) == None:
            utime_dict[record_n] = u_time
        else:
            utime_dict[record_n] += u_time
    # 입차는 했지만 출차기록이 없는 경우 -> 23:59 출차처리
    for k, v in check_dict.items():
        v_h, v_m = map(int, v.split(":"))
        if utime_dict.get(k) == None:
            utime_dict[k] = (23 - v_h) * 60 + (59 - v_m)
        else:
            utime_dict[k] += (23 - v_h) * 60 + (59 - v_m)
    # (key, value) 형태를 요소로하는 리스트를 만든후 빠른 차번호(key)순서로 정렬
    temp = sorted(list(utime_dict.items()), key = lambda x : x[0])
    for n, t in temp:
        fee = fees[1]
        # 사용시간이 기본시간 이상일때 추가요금 계산
        if t > fees[0]:
            unit_time = (t - fees[0]) / fees[2]
            # 단위시간 계산시 올림처리
            if int(unit_time) < unit_time:
                unit_time = int(unit_time) + 1
            fee += unit_time * fees[3]
        answer.append(fee)
    # 요금 리스트 생성후 반환
    return answer