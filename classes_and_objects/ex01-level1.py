from collections import Counter

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

tamanho = len(ages)
for i in range(tamanho-1): 
    for j in range(tamanho-i-1):
        if ages[j] > ages[j+1]:
            ages[j], ages[j+1] = ages[j+1], ages[j]
print(ages)

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)
    
    def sum(self):
        soma = 0
        for n in range(len(ages)):
            soma += ages[n]
        return soma

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return range(self.data)

    def mean(self):
        media = round(sum(self.data)/len(self.data))
        return media

    def median(self):
        return self.data[int(len(self.data)/2)]

    def mode(self):
        nr = []
        nr = Counter(self.data)
        return nr.most_common(1)
        
    def std(self):
        pass

    def var(self):
        pass

    def freq_dist(self):
        pass

    def describe(self):
        print('Count: ',data.count())
        print('Sum: ', data.sum())
        print('Min: ', data.min())
        print('Max: ', data.max())
        print('Mean: ', data.mean())
        print('Median: ', data.median())
        print('Mode: ', data.mode())

data = Statistics(ages)
data.describe()