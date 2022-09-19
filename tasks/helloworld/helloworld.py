# s = input()
# print('Hello, ' + s + '!')

# a = int(input())
# print(a + 1)

# print('Hello "World"!')
# print("Hello \"World\"!")

# print((1 + 2) * 3 ** 0.37)

# s = 'abcd'
# print(s[0])
#
# a = [1, 2, 3, 4, 5]
# print(a[2])

# a, b, c = map(int, input().split())

# max(a, b, c) < sum 2 remaining
# 2 * max(a, b, c) < a + b + c

# if 2 * max(a, b, c) < a + b + c:
#     print('Triangle OK')
# elif 2 * max(a, b, c) == a + b + c:
#     print('Segment')
# else:
#     print('Ne ok')

a = list(map(int, input().split()))

# for (int i = 0; i < n; i++) ...
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)



print(*b)
print(' '.join(map(str, b)))

print('------------')

# for (int i = 0; i < 10; i++) ...
for i in range(18, 3, -1):
    print(i ** 3)