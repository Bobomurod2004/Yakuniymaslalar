def yigindi(son):
    if not son:
        return 0
    return son[0] + yigindi(son[1:])
nums = [1,2,3,4]
print(yigindi(nums))
