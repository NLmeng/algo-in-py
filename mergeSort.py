

def merge_sort(nlist, start, end):
    #sorts the list from indexes start to end - 1 inclusive
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(nlist, start, mid)
        merge_sort(nlist, mid, end)
        merge_list(nlist, start, mid, end)
 
def merge_list(nlist, start, mid, end):
    left = nlist[start:mid]
    right = nlist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
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