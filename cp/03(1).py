counter = 0

while True:
    nums = [int(x) for x in input().split("; ")]
    res = list()

    if "100500" in [str(x) for x in nums]:
        break

    for x in nums[1:]:
        if x % nums[0] == 0 and x not in res:
            res.append(x)

    print(" ".join([str(x) for x in sorted(res)]), end=" ")
    print(max(res) if counter % 2 == 0 else min(res))

    counter += 1