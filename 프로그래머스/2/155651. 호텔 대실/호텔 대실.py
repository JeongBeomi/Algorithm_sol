from collections import deque

def solution(book_time):
    answer = 0
    # 끝나는 시간, 시작시간 순으로 정렬
    book_time.sort(key = lambda x : (x[0], x[1]))
    q = []
    
    for book in book_time:
        # 대실이 종료된 방은 빼준다
        q.sort(reverse = True)
        while q and q[-1] <= book[0]:
            q.pop()
        
        # 대실 종료시간에 10분을 더해서 q에 넣어준다
        book = book[1].split(":")
        book[0], book[1] = str(int(book[0]) + (int(book[1]) + 10) // 60), str((int(book[1]) + 10) % 60)
        # 시간이 한자리수일때 앞에 0을 넣어준다
        book[0], book[1] = (2 - len(book[0])) * "0" + book[0], (2 - len(book[1])) * "0" + book[1]
        q.append(":".join(book))
        
        # 방 개수가 최대이면 갱신
        if len(q) > answer:
            answer = len(q)
    return answer