'''
Stephen O'Donovan
102554291

Bubblesort is by far the least efficient sorting algorithm,
taking nearly half a minute to sort lists of size ~10000

The Python in built sorting function is the fastest, being at
least one order of magnitude faster than any other function

Quicksort is the fastest of the three other functions

Mergesort is generally slightly faster than Heapsort

As expected, Quicksort deals with all list variations
in close to the same time due to Quicksort
randomising every list that is passed to it

Bubblesort performs best with a sorted list and runs noticably
slower with a reversed list

Heapsort runs similarly for three of the lists but is noticably slower
for a sorted list

Mergesort runs fastest for sorted lists and slowest for shuffled lists

The Python sort function performs fastest with a sorted list and
slowest with a shuffled list

'''

import random, time, sys
sys.setrecursionlimit(1000)

def evaluate():

    evaluateall(100, 0, 10)
    evaluateall(1000, 0, 100)
    evaluateall(10000, 0, 1000)
    evaluateall(100000, 0, 1000)
    evaluateall(100, 20, 10)
    evaluateall(1000, 200, 100)
    evaluateall(10000, 2000, 1000)
    evaluateall(100000, 20000, 10000)
    evaluateall(100, 70, 10)
    evaluateall(1000, 700, 100)
    evaluateall(10000, 7000, 1000)
    evaluateall(100000, 70000, 10000)
    
def evaluateall(n, k, p):

    base_list = []
    
    for i in range (n-k):
        base_list.append(i)
    for _i in range (n-k, n):
        base_list.append(random.randint(0, n-k-1))

    sorted_list = sorted(base_list)
    reverse_list = sorted_list[n::-1]

    partial_list = sorted_list[:]
    for _i in range (p):
        j = random.randint(0, n-1)
        m = random.randint(0, n-1)
        while m == j:
            m = random.randint(0, n-1)
        partial_list[j], partial_list[m] = partial_list[m], partial_list[j] 

    shuffle_list = sorted_list[:]
    random.shuffle(shuffle_list)
    
    sort_list = [bubblesort, quicksort,
                 mergesort, heapsort,
                 pythonsort]
    
    list_dict = {'sorted': sorted_list, 'reverse': reverse_list,
                 'partial': partial_list, 'shuffle': shuffle_list}
    
    for test_list in list_dict:
        for test_sort in sort_list:
            if n > 10000 and test_sort.__name__ == 'bubblesort':
                print('Skipping bubblesort for this list')
                continue
            result = test(test_sort, list_dict[test_list])
            if type(result) == str:
                print (result)
            else:
                print ('%-15.9f %-10s %-10s %5d %5d %5d' % (
                        result, test_list, test_sort.__name__,
                        n, k, p )
                      )

def test(f, inlist):

    test_list = inlist[:]
    if f.__name__ == 'pythonsort':
        result_list = f(test_list)
        result = result_list[0]
        test_list = result_list[1]
    elif f.__name__ == 'quicksort':
        result = 0
        for i in range(5):
            start_time = time.perf_counter()
            f(test_list)
            end_time = time.perf_counter()
            result += (end_time - start_time)
        result /= 5
    else:
        start_time = time.perf_counter()
        f(test_list)
        end_time = time.perf_counter()
        result = end_time - start_time
    if check(test_list):
        return result
    return '***Error: incorrectly sorted list***'

def check(testlist):

    i = 0
    end = len(testlist) - 1
    errors = False
    while i < end and errors == False:
        if testlist[i] > testlist[i+1]:
            errors = True
            break
        i += 1

    if errors:
        return False
    else:
        return True

def pythonsort(test_list):
    
    start_time = time.perf_counter()
    test_list = sorted(test_list)
    end_time = time.perf_counter()
    result = end_time - start_time
    return [result, test_list]

def bubblesort(mylist):

    length = len(mylist)
    for i in range(length):
        for j in range(length - 1 - i):
            if mylist[j] > mylist[j + 1]:
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
    return mylist
    
def heapsort(inlist):

    length = len(inlist)
    for i in range(length):
        bubbleup(inlist, i)
    for i in range(length):
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist, 0, length - 2 - i)

def bubbleup(inlist, i):

    while i > 0 :
        parent = (i - 1) // 2
        if inlist[i] > inlist[parent]:
            inlist[i], inlist[parent] = inlist[parent], inlist[i]
            i = parent
        else:
            i = 0

def bubbledown(inlist, i, last):

    while last > (i*2):
        lc = i*2 + 1
        rc = i*2 +2
        maxc = lc
        if last > lc and inlist[rc] > inlist[lc]:
            maxc = rc
        if inlist[i] < inlist[maxc]:
            inlist[i], inlist[maxc] = inlist[maxc], inlist[i]
            i = maxc
        else:
            i = last

def quicksort(mylist):

    n = len(mylist)
    for i in range(len(mylist)):
        j = random.randint(0, n-1)
        mylist[i], mylist[j] = mylist[j], mylist[i]
    return _quicksort(mylist, 0, n-1)

def _quicksort(mylist, first, last):

    if last > first:
        pivot = mylist[first]
        f = first + 1
        b = last

        while f <= b:
            while f <= b and mylist[f] < pivot:
                f +=1
            while f <= b and mylist[b] > pivot:
                b -= 1
            if f <= b:
                mylist[f], mylist[b] = mylist[b], mylist[f]
                f += 1
                b -= 1
        mylist[b], mylist[first] = mylist[first], mylist[b]
        _quicksort(mylist, first, b - 1)
        _quicksort(mylist, b + 1, last)

    return mylist

def mergesort(mylist):

    n = len(mylist)
    if n > 1:
        list1 = mylist[:n//2]
        list2 = mylist[n//2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)
    
    return mylist

def merge(list1, list2, mylist):

    f1 = 0
    f2 = 0
    while f1 + f2 < len(mylist):
        if f1 == len(list1):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            mylist[f1+f2] = list2[f2]
            f2 += 1
        else:
            mylist[f1+f2] = list1[f1]
            f1 += 1
    return mylist

evaluate()
