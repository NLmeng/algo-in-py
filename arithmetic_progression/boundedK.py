

def findCK(Array, K):
    n   = len(Array)
    first = Array[0]
    last  = Array[n-1]

    if(n < K + 2 or len(Array) < 2):
        return ValueError('Invalid Array Length')

    prev = Array[0]
    curr_c = last - first
    ind = 1
    while ind < n:
        curr_c = min(curr_c, Array[ind] - prev)
        prev = Array[ind]
        ind += 1
    return curr_c, ((last - first) / curr_c) - n + 1



#
#
arr = [6, 10]; 
print("c, k: (4, 0)", findCK(arr, 0)); 

arr = [3, 6, 9]; 
print("c, k: (3, 0)", findCK(arr, 1)); 

arr = [4, 16, 22, 25, 28, 31]; 
print("c, k: (3, 4)", findCK(arr, 4)); 

arr = [4, 16, 20, 28, 32]; 
print("c, k: (4, 3)", findCK(arr, 3)); 

arr = [4, 10, 16, 28]; 
print("c, k: (6, 1)", findCK(arr, 2)); 

arr = [4, 16, 28]; 
print("c, k: (12, 0)", findCK(arr, 1)); 

arr = [0, 15, 20, 25, 35, 45, 50, 55, 60, 65, 75]; 
print("c, k: (5, 5) ", findCK(arr, 9)); 
#
#