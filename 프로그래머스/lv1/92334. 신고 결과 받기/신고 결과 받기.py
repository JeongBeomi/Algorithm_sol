def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported = {}
    
    # key 값의 유저를 신고한 사람을 value 리스트에 추가    
    for report_string in report:
        user_id, report_id = report_string.split()
        #딕셔너리 내부에 존재하지 않으면 새로 생성
        if reported.get(report_id) == None:
            reported[report_id] = set([user_id])
        #딕셔너리 내부에 존재할 때는 해당 value 리스트에 추가
        else:
            reported[report_id].add(user_id)
    
    # 출력을 위한 정지 메일 수 확인
    for user_name in reported.keys():
        user_list = reported.get(user_name)
        if len(user_list) >= k:
            for user in user_list:
                answer[id_list.index(user)] += 1
            
    return answer