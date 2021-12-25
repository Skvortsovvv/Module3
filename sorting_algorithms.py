import random


def buble_sort(massive: list):
    for i in range(0, len(massive)):
        for j in range(0, len(massive) - i - 1):
            if massive[j] > massive[j+1]:
                massive[j], massive[j+1] = massive[j+1], massive[j]
    return massive


def selection_sort(massive: list):
    for i in range(0, len(massive)):
        min_index = i
        for j in range(i, len(massive)):
            if massive[j] <= massive[min_index]:
                min_index = j
        massive[i], massive[min_index] = massive[min_index], massive[i]
    return massive


def merge_sort(massive: list):
    if len(massive) == 0 or len(massive) == 1:
        return massive
    else:
        left = massive[:len(massive)//2]
        right = massive[len(massive)//2:]
        merge_sort(left)
        merge_sort(right)
        C = [0] * (len(left) + len(right))
        n = m = k = 0
        while n < len(left) and m < len(right):
            if left[n] <= right[m]:
                C[k] = left[n]
                n += 1
            else:
                C[k] = right[m]
                m += 1
            k += 1
        while n < len(left):
            C[k] = left[n]
            n += 1
            k += 1
        while m < len(right):
            C[k] = right[m]
            m += 1
            k += 1
        for i in range(len(massive)):
            massive[i] = C[i]
        return massive


def partition(massive, p, r):
    s = random.randint(p, r)
    b = massive[s]
    massive[s], massive[r] = massive[r], massive[s]
    i = p
    for j in range(p, r):
        if massive[j] < b:
            massive[i], massive[j] = massive[j], massive[i]
            i += 1
    massive[i], massive[r] = massive[r], massive[i]
    return i


def quick_sort(massive: list, p, r):
    if p < r:
        q = partition(massive, p, r)
        quick_sort(massive, p, q-1)
        quick_sort(massive, q+1, r)
    return massive


def count_sort(massive: list):
    k = max(massive)
    C = [0] * (k+1)
    for i in range(0, len(massive)):
        C[massive[i]] += 1
    for j in range(1, k+1):
        C[j] += C[j-1]
    B = [0] * len(massive)
    for i in range(len(massive)-1, -1, -1):
        C[massive[i]] -= 1
        B[C[massive[i]]] = massive[i]
    return B


def insert_sort(massive: list):
    for i in range(1, len(massive)):
        for j in range(i, 0, -1):
            if massive[j] < massive[j-1]:
                massive[j], massive[j-1] = massive[j-1], massive[j]
            else:
                break
    return massive


if __name__ == "__main__":

    l = [2, 6, 1, 7, 2, 4, 3, 5, 0]
    ll = [6, 5, 9, 3, 7, 4, 7]
    print(buble_sort(ll))
    print(selection_sort(ll))
    print(merge_sort(ll))
    print(quick_sort(ll, 0, len(ll)-1))
    print(count_sort(ll))
    print(insert_sort(ll))
