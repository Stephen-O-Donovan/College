import random, copy, time

def bubbleup(inlist):

    length = len(inlist)

    for i in range(length):

        while i > 0 :
            parent = (i - 1) // 2
            if inlist[i] > inlist[parent]:
                inlist[i], inlist[parent] = inlist[parent], inlist[i]
                i = parent
            else:

def test(f, inlist):

    start_time = time.perf_counter()
    f(inlist)
    end_time = time.perf_counter()
    result = str(f.__name__) + ' ' \
            + str(inlist) + ' ' + str(end_time - start_time)
    return result

testlist = [2, 5, 1, 3, 4]
print(test(bubbleup, testlist))
