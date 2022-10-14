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
    return(findInSplit(Array, n, c))

def findInSplit(sub, size, c):
    missing = []
    if size == 2:
        start = sub[0]
        end   = sub[size - 1]
        while start + c < end:
            start = start + c
            missing.append(start)
    else:
        midL  = ceil(len(sub) / 2)
        midR  = len(sub) // 2
        
        L = sub[:midL]
        R = sub[midR:]

        missing.append(findInSplit(L, len(L), c))

        if (L[midL-1] + c != R[0]):
            missing.append(findInSplit([L[midL-1], R[0]], 2, c))

        missing.append(findInSplit(R, len(R), c))

    return missing
#
#
arr = [0, 4, 10]; 
print("The missing elements are", findAll(arr, 3), len(findAll(arr,3))); 
arr = [3, 4, 13]; 
print("The missing elements are", findAll(arr, 8), len(findAll(arr,8))); 
arr = [3,13]
print("The missing elements are", findAll(arr, 9), len(findAll(arr,9))); 
arr = [0,20,50,70,100]
print("The missing elements are", findAll(arr, 6), len(findAll(arr,6))); 
arr = [3,6,12,18,24,27]
print("The missing elements are", findAll(arr, 3), len(findAll(arr,3))); 
arr = [3,12,27]
print("The missing elements are", findAll(arr, 6), len(findAll(arr,6))); 
arr = [4, 10, 13, 19, 28, 31, 40, 52]
print("The missing elements are", findAll(arr, 9), len(findAll(arr,9))); 
#
#