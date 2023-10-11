def solution(record):
    answer = []
    userid_to_nickname = dict()
    c_dict = {
        "Enter" : "님이 들어왔습니다.",
        "Leave" : "님이 나갔습니다."
    }
    temp = []
    
    for r in record:
        r = r.split()
        if r[0] != "Leave":
            userid_to_nickname[r[1]] = r[2]
            
        if r[0] in c_dict:
            temp.append((r[1], c_dict[r[0]]))
    
    for userid, text in temp:
        answer.append(userid_to_nickname[userid] + text)

    return answer