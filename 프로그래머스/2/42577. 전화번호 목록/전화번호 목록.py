def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : len(x))
    visited = set([phone_book[0]])
    number_length = len(phone_book[0])
    for i in range(1, len(phone_book)):
        for j in range(1, number_length + 1):
            if phone_book[i][0 : j] in visited:
                answer = False
                return answer
        visited.add(phone_book[i])
        number_length = max(number_length, len(phone_book[i]))
            
    return answer