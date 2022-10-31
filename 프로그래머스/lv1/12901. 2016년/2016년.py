def solution(a, b):
    m = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = sum(m[:a]) + b
    d %= 7 
    w = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    return w[d]