n = int(input())
words = [input() for _ in range(n)]
words.sort(key=len)
result = n

# 길이가 짧은 단어가 다른 단어의 접두사면 제외시킨다
for i in range(n):
    for j in range(i + 1, n):
        if words[i] == words[j][0 : len(words[i])]:
            result -= 1
            break

print(result)
