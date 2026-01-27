sum_even = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0: 
        sum_even += i
    else:
        sum_odds += i

print(f'The sum of all evens is {sum_even}. And the sum of all ods is {sum_odds}')