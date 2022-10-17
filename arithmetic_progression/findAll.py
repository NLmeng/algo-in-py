from math import ceil

# c = common difference, k = missing numbers
# goal: O(k + logn)


# @param Array with k missing numbers, always given Last and First
# @return array sized k of missing numbers
def findAll(Array, k):
    n      = len(Array)
    first  = Array[0]
    last   = Array[n-1]
    c      = (last - first) // (n + k - 1)
    print(c, (n + k - 1))
    return(findInSplit(Array, 0, n-1, c))

def findInSplit(sub, startIndex, endIndex, c):
    missing = []

    if endIndex - startIndex == 1:
        start = sub[startIndex]
        end   = sub[endIndex]
        while start + c < end:
            start = start + c
            missing.append(start)
    else:
        mid  = (endIndex + startIndex) // 2

        missing.append(findInSplit(sub, startIndex, mid, c))
        missing.append(findInSplit(sub, mid, endIndex, c))

    return missing

#
#
arr = [0, 4, 10]; 
print("The missing elements are", findAll(arr, 3)); 
arr = [3, 4, 13]; 
print("The missing elements are", findAll(arr, 8)); 
arr = [3,13]
print("The missing elements are", findAll(arr, 9)); 
arr = [4, 336, 834, 1000]
print("The missing elements are", findAll(arr, 3)); 
arr = [0,20,50,70,100]
print("The missing elements are", findAll(arr, 6)); 
arr = [3,6,12,18,24,27]
print("The missing elements are", findAll(arr, 3)); 
arr = [3,12,27]
print("The missing elements are", findAll(arr, 6)); 
arr = [4, 10, 13, 19, 28, 31, 40, 52]
print("The missing elements are", findAll(arr, 9)); 
#
#