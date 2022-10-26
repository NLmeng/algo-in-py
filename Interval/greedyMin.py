


from operator import ne
from re import I


def mergeSortLFF(nlist, start, end):
    #sorts the list from indexes start to end - 1 inclusive
    if end - start > 1:
        mid = (start + end)//2
        mergeSortLFF(nlist, start, mid)
        mergeSortLFF(nlist, mid, end)
        mergeLFF(nlist, start, mid, end)
 
def mergeLFF(nlist, start, mid, end):
    left = nlist[start:mid]
    right = nlist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i][1] <= right[j][1]):
            nlist[k] = left[i]
            i = i + 1
        else:
            nlist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            nlist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            nlist[k] = right[j]
            j = j + 1
            k = k + 1

def greedyMin(V):
    mergeSortLFF(V,0,len(V))
    V.reverse()
    # print(V)
    currentMin = []
    index = 0
    currentTime = V[index][0]
    currentBest = V[index][0]

    curr = 0
    while curr < len(V):
        next = curr + 1

        if next >= len(V):
            currentMin.append(V[index])
        # check overlap
        elif V[next][1] > currentTime:
            if V[next][0] < currentBest:
                currentBest = V[next][0]
                index = next
        # not overlap
        else:
            # not overlapping with earliest
            if V[next][1] <= currentBest:
                currentMin.append(V[index])
                currentBest = V[next][0]
                currentTime = V[next][0]
                index = next
        
        curr = next


    return currentMin

print(1, greedyMin([(0,5)]))
print(2, greedyMin([(0,5), (5,8)]))
print(1, greedyMin([(0,6), (5,8), (7,10)]))
print(3, greedyMin([(0,4), (4,6), (6,10)]))
print(2, greedyMin([(1,3),(2,4),(3,4),(3,5),(4,5),(4,6),(5,7)]))
print(3, greedyMin([(0,2), (1,4), (3,10), (5,6), (7,8), (9,10), (12,15)]))
print(2, greedyMin([(1,4), (3,5), (0,6), (4,7), (3,8), (5,9), (6,10), (8,11)]))