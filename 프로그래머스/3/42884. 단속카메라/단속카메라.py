def solution(routes):
    cameras = []
    routes.sort()
    for route in routes:
        if not cameras:
            cameras.append(route)
            continue
        check = 1
        for i, camera in enumerate(cameras):
            if route[0]>camera[1]:
                continue
            cameras[i] = [max(route[0], camera[0]), min(route[1], camera[1])]
            check = 0
            break
        if check:
            cameras.append(route)
    return len(cameras)