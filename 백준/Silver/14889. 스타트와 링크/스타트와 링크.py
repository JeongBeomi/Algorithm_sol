def team(s, e):
    global answer
    if len(start_team) == n // 2:
        result = cal()
        if answer > result:
            answer = result
        return
    
    for i in range(s, e):
        start_team.append(members[i])
        team(i + 1, e)
        start_team.pop()
  
def cal():
    link_team = list(set(members) - set(start_team))
    score_list = []
    for team in (start_team, link_team):
        temp = 0
        for i in range(len(team) - 1):
            for j in range(i + 1, len(team)):
                temp += status[team[i] - 1][team[j] - 1]
                temp += status[team[j] - 1][team[i] - 1]
        score_list.append(temp)
    
    return abs(score_list[0] - score_list[1])

n = int(input())
answer = n * 2 * 100
status = [list(map(int, input().split())) for _ in range(n)]
members = list(range(1, n + 1))
start_team = []

team(0, n)
print(answer)