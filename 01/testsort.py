import time, random
from sorters import Sorters

class Testsort():

    def test(f, inlist):

        start_time = time.perf_counter()
        f(inlist)
        end_time = time.perf_counter()
        result = str(f.__name__) + ' ' \
                + str(inlist) + ' ' + str(end_time - start_time)
        return [result, (end_time - start_time)]

    def randsort(listnum):
        randlist = []

        for i in range(listnum+1):
            randlist.append(i)

        n = len(randlist)
        for i in range(n):
             
            j = random.randint(0, n - 1)
            randlist[i], randlist[j] = randlist[j], randlist[i]
        return randlist

    def comparisons():
        for i in range(100):
            quicksort = (Testsort.test(Sorters.quicksort, randlist)[1])
            mergesort = (Testsort.test(Sorters.mergesort, randlist)[1])
            heapsort = (Testsort.test(Sorters.heapsort, randlist)[1])
            bubblesort = (Testsort.test(Sorters.heapsort, randlist)[1])
            if (quicksort < mergesort and quicksort < heapsort
                and quicksort < bubblesort):
                print('quicksort wins')
            elif (mergesort < heapsort and mergesort < bubblesort):
                print('mergesort wins')
            elif (heapsort < bubblesort):
                print('heapsort wins')
            else:
                print('bubblesort wins')
                     
randlist = Testsort.randsort(100)
#print(randlist)
print(Testsort.test(Sorters.bubblesort, randlist)[1])

print(Testsort.test(Sorters.quicksort, randlist)[1])
print(Testsort.test(Sorters.mergesort, randlist)[1])
print(Testsort.test(Sorters.heapsort, randlist)[1])
#Testsort.comparisons()
