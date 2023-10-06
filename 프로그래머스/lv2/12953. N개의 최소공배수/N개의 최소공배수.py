def solution(arr):
    answer = 0
    arr.sort()
    while len(arr) > 1:
        num1, num2 = arr.pop(), arr.pop()
        least_common_multiple = num1 * num2
        
        # 유클리드 호제법 최소공약수 구하는 방법
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        
        least_common_multiple //= num1
        
        arr.append(least_common_multiple)
    answer = arr[0]
    return answer