from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque()
    s = 0
    while trucks:
        truck = trucks.popleft()
        if len(bridge) == bridge_length:
            s -= bridge.popleft()
        while s + truck > weight:
            bridge.append(0)
            answer += 1
            if len(bridge) == bridge_length:
                s -= bridge.popleft()
        bridge.append(truck)
        s += truck
        answer += 1
        
    answer += bridge_length
    return answer

