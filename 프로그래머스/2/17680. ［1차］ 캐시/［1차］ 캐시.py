def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        city = city.upper()
        for i, c in enumerate(cache):
            if c == city:
                answer += 1
                cache.append(cache.pop(i))
                break
        else:
            answer += 5
            cache.append(city)
            while len(cache) > cacheSize:
                cache.pop(0)   
    return answer