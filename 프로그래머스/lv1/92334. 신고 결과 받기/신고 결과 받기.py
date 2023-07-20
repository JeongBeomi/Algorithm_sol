def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported = {id : [] for id in id_list}
    
    # key 값의 유저를 신고한 사람을 value 리스트에 추가    
    for report_string in set(report):
        user_id, report_id = report_string.split()
        reported[report_id].append(user_id)
    
    # 출력을 위한 정지 메일 수 확인
    for user_name in reported.keys():
        user_list = reported.get(user_name)
        if len(user_list) >= k:
            for user in user_list:
                answer[id_list.index(user)] += 1
            
    return answer