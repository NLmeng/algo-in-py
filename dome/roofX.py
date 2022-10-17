#
def a():
    return

# splits into halves, and build on each halves
def buildDomeRecursive(arr):
    size = len(arr)
    if size > 1:
        mid = size // 2
        left_half  = arr[:mid]
        right_half = arr[mid:]
        # each call is a subproblem that will choose appropriate edges
        left_edges  = buildDomeRecursive(left_half)
        right_edges = buildDomeRecursive(right_half)
        # all call will be merged in buildDome
        return buildDome(left_half, right_half, left_edges, right_edges)

# handle each cases for appropriate dome
def buildDome(left_arr, right_arr, left_edges, right_edges):
    # edges will initially be empty
    if left_edges is None:
        left_edges  = []

    if right_edges is None:
        right_edges = []

    # identify min and max on left halves
    l_max = max(left_arr, key=lambda item:item[1])
    l_min = min(left_arr, key=lambda item:item[1])
    # print(left_arr, l_max, l_min)

    # merging left and right edges
    edges = []

    # initially left and right will be empty
    edge_left  = None
    edge_right = None

    # CASE 1: if all on left shorter than right 
    #         -> connect tallest in left to leftmost in right
    # ??? if max on left shorter than leftmost in right
    if all(l_max[1] < tup[1] for tup in right_arr):
        print(right_arr)
        edge_left  = l_max[0]
        edge_right = right_arr[0][0]

    # CASE 2: if all on left side taller than right 
    #         -> connect rightmost on left side to tallest in right
    # ??? if min on left taller than tallest in right
    elif all(l_min[1] > tup[1] for tup in right_arr):
        edge_left  = left_arr[-1][0]
        edge_right = max(right_arr, key=lambda item:item[1])[0]

    # CASE 3: if some on right taller than tallest in left 
    #         -> connect tallest in left to first taller in right
    elif any(tup[0] for tup in right_arr if tup[1] > l_max[1]):
        edge_left  = l_max[0]
        edge_right = next(tup[0] for tup in right_arr if tup[1] > l_max[1])

    # CASE 4: if nothing is taller than tallest in left
    #         -> connect tallest in left to the next tallest
    else:
        # array of all buildings taller than l_max
        left_arr_index_gt_max = [tup for tup in left_arr if tup[0] > l_max[0]]

        # find next tallest after l_max 
        if left_arr_index_gt_max == []:
            l_max_after_max = None
        else:
            l_max_after_max = max(left_arr_index_gt_max, key=lambda item:item[1])

        # find tallest building in right side
        r_max = max(right_arr, key=lambda item:item[1])

        # if tallest building ???
        if l_max_after_max is not None and l_max_after_max[0] > r_max[0]:
            # loop through left array, ???
            for i in range(len(left_arr_index_gt_max)):
                if edge_left == None:
                    edge_left = left_arr_index_gt_max[i][0]
                elif left_arr_index_gt_max[i][1] > r_max[1] and any(tup[0] for tup in left_edges
                if tup(0) == left_arr_index_gt_max[i][0] or tup[1] == left_arr_index_gt_max[i][0]):
                    edge_left = left_arr_index_gt_max[i][0]

            # if no edge qualifies, connect l_max to r_max
            if edge_left == None:
                edge_left = l_max[0]
        
        # if right side has next tallest after l_max, connect l_max to r_max
        else:
            edge_left = l_max[0]
        edge_right = r_max[0]

    # add all edges in left up till the chosen left edge
    for t in left_edges:
        if t[0] < edge_left:
            edges.append(t)
        else:
            break

    edges.append(tuple((edge_left, edge_right)))

    for t in right_edges:
        if t[0] >= edge_right:
            edges.append(t)

    return edges


arr1 = [(1,4), (2,6), (3,5), (4,1), (5,8), (6,6), (7,2), (8,3)]
print(buildDomeRecursive(arr1))

# arr2 = [(1,4), (2,3), (3,5), (4,1), (5,8), (6,7), (7,2), (8,3)]
# print(buildDomeRecursive(arr2))

# arr3 = [(1,1), (2,2), (3,3)]
# print(buildDomeRecursive(arr3))

# arr4 = [(1,1), (2,2), (3,3), (4,2)]
# print(buildDomeRecursive(arr4))