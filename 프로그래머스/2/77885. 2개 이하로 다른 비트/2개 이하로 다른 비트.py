def f(x):
    n = 0
    num = x
    while num % 2:
        n += 1
        num //= 2
    if (n != 0) :
        n -= 1
    
    return x + (2**n)
    
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(f(num))
    return answer