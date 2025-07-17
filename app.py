import random

def random_number():
    zahlen = []
    i = 0
    while i < 10:
        i += 1
        zahlen = zahlen + [random.randint(1, 10)]
    print("unsorted:", zahlen)
    return zahlen

def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

zahlen = random_number()
sortiert = bubble_sort(zahlen)
print("\nsorted:  ", sortiert)
