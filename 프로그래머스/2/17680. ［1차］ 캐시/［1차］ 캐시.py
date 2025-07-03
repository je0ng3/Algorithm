def get(cache, city, cacheSize):
    if cacheSize and len(cache)==cacheSize:
        cache = cache[1:]
    if len(cache)<cacheSize:
        cache.append(city)
    return cache

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer +=1
        else:
            cache = get(cache, city, cacheSize)
            answer += 5
    return answer