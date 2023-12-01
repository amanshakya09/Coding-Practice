def dailyTemperatures(tmpr):
    stk = []
    ans = [0] * len(tmpr)
    for i in range(len(tmpr)):
        if not stk or tmpr[stk[-1]] >= tmpr[i]:
            stk.append(i)
        else:
            while stk and tmpr[i] > tmpr[stk[-1]]:
                x = stk.pop()
                ans[x] = i - x
            stk.append(i)
    return ans


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
