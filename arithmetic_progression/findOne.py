# overview: solve for c, if nth position is at mid, then the missing is right else left
# O(logn)
def findOne(subArr, n):
    if n == 2:
        return (subArr[0] + subArr[1])/2
    
    low  = 0
    high = n-1
    c    = min(subArr[1] - subArr[0], subArr[2] - subArr[1])

    while low < high-1:
        mid = (low + high) // 2

        if subArr[mid] - subArr[low] == c * (mid - low):
            low = mid
        else:
            high = mid

    return subArr[low] + c