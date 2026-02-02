""""stop = int(input('Em que numero vc pretende parar? (1-20)\n'))

for i in range(1, 21):
    if i == stop:
        break
    print(i, end=" ")

"""


#nested loops. an example using coordinates


''''for x in range(7):
    for y in range(3):
        print(f'{(x, y)}')'''

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        continue
    print(x)
print(f'We have {count} even numbers.')


nums = [0, 1, 2, 4, 3, 5, 8, 10]


for x in range(len(nums)):
    if nums[x] == 3:
        posicao = x
print(nums)
print(f'Foi encontrado na posicao {posicao+1}')
