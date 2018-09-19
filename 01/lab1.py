
import random
import copy
import time

def heapsort(inlist):

    length = len(inlist)
    for i in range(length):
        bubbleup(inlist, i)
    print(inlist)

    for i in range(length):
        inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
        bubbledown(inlist, 0, length - 2 - i)
    print(inlist)

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

def test(inlist):

    start_time = time.perf_counter()
    heapsort(inlist)
    if check(inlist) == -1:
        return ('Error')
    end_time = time.perf_counter()
    #result = str(inlist) + ' time taken ' + str(end_time - start_time)
    return end_time - start_time

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
        return -1
    else:
        return 0

def testrandom(n):
    testlist = [i for i in range(n)]
    random.shuffle(testlist)
    #print('testlist is : ', end = '')
    #print(testlist)
    return test(testlist)

#print( testrandom(6) )
print( testrandom(10) )
#print( testrandom(20) )


