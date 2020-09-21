def who_is_next(names, r):
    sum = len(names)
    i = 1
    while sum < r:
        sum += (2**i)*len(names)
        i += 1
    return names[n - (sum - r)//(2**(i-1))-1]

#sum - r = sobra um número entre 0 e n*(2**(i-1))

names = [ 'a', 'b', 'c']#, 'd', 'e', 'f', 'g' ]
print(who_is_next(names, 6))


# def who_is_next(names, r):
#     line = list(names)
#     c = 1
#     while len(line) < r:
#         line.extend([line[c-1], line[c-1]])
#         c += 1
#     return line[r-1]
#
# def who_is_next2(names, r):
#     x = int(r)
#     while  x > len(names):
#         x = (x - x%2)//2 - len(names)//2
#     return names[x-1]



# names = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
# for i in range(990001):
#     if who_is_next(names, i) != who_is_next2(names, i):
#         print("Zebra")
#         break
# print("OK")

# print("Input:", 52)
# print("Método 1:", who_is_next(names, 20))
# print("Método 2:", who_is_next2(names, 20))
#
# print("Input:", 222233)
# print("Método 1:", who_is_next(names, 2222233))
# print("Método 2:", who_is_next2(names, 2222233))
