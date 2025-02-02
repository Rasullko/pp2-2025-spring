def spy_game(nums):
    ind = 0
    cnt = 0
    a = []
    for i in range(len(nums)):
        if nums[i] == 0:
            a.append(i)
            cnt = cnt + 1
        if nums[i] == 7:
            ind = i
    for i in a:
        if cnt >= 2 and ind > i:
            return True
    return False

nums = list(map(int, input().split()))
print(spy_game(nums))