import numpy as np

m = int(input("What is the height of rails?"))
# m = 3
a = np.ndarray(shape=(m, m))
creation_patterns = np.zeros(shape=(m, m)).astype(int)

for i in range(m):
    for j in range(m):
        if j < i:
            a[i, j] = 0
        else:
            a[i, j] = 1


def ways_to_paint_region(rail : list, must_be):
    """Easily optimisable with math"""
    paintings = 0
    for i in range(len(rail)):
        for j in range(len(rail)):
            painted = rail[i:j+1]
            if all(must_be_present in painted for must_be_present in np.unique(must_be)):
                paintings += 1
    return paintings


for i in range(m):
    for j in range(m):
        if j < i:
            creation_patterns[i, j] = 0
        else:
            classn = np.empty(shape=[4])
            classn[0] = ways_to_paint_region(list(range(i, j + 1)), [i, j]) * (i + 1) * (m - j)
            classn[1] = ways_to_paint_region(list(range(i, j)), [i]) * (i + 1)
            classn[2] = ways_to_paint_region(list(range(i + 1, j + 1)), [j]) * (m - j)
            classn[3] = ways_to_paint_region(list(range(i + 1, j)), [])
            creation_patterns[i, j] = sum(classn)

print("Below matrix says, in how many ways you can paint next rail, if previous one was pained in a specific way:")
print(creation_patterns)
print("ie:")
for i in range(m):
    for j in range(m):
        print(f"{creation_patterns[i, j]} at [{i},{j}] means"
              f", that if you painted {i}-{j} region (both inclusive)"
              f", then there are {creation_patterns[i, j]} ways of painting next rail")

