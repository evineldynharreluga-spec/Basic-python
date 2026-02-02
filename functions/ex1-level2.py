def evens_and_odds(number):
    count_even = 0
    count_odds = 0
    for i in range(0, number+1):
        if i % 2 == 0:
            count_even +=1
        else:
            count_odds += 1
    print(f'The number of odds are {count_odds}.\nThe number of evens are {count_even}.')
    
evens_and_odds(100)
