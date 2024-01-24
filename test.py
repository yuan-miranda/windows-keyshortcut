a = [10, 20]
b =  {
    (10, 20): "c",
    (20, 30): "d"
}

for i, j in b.items():
    print(i, j)
    if tuple(a) == i:
        print("yes")