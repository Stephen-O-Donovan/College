class Sorters():

    def quicksort(mylist):

        n = len(mylist)
        return Sorters._quicksort(mylist, 0, n-1)

    def _quicksort(mylist, first, last):

        if last > first:
            pivot = mylist[first]
            f = first + 1
            b = last

            while f <= b:
                while f <= b and mylist[f] <= pivot:
                    f +=1
                while f <= b and mylist[b] >= pivot:
                    b -= 1
                if f < b:
                    mylist[f], mylist[b] = mylist[b], mylist[f]
                    f += 1
                    b -= 1
            mylist[b], mylist[first] = mylist[first], mylist[b]
            Sorters._quicksort(mylist, first, b - 1)
            Sorters._quicksort(mylist, b + 1, last)

        return mylist

    def mergesort(mylist):

        n = len(mylist)
        if n > 1:
            list1 = mylist[:n//2]
            list2 = mylist[n//2:]
            Sorters.mergesort(list1)
            Sorters.mergesort(list2)
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

    def heapsort(inlist):

        length = len(inlist)
        for i in range(length):
            Sorters.bubbleup(inlist, i)
        for i in range(length):
            inlist[0], inlist[length - 1 - i] = inlist[length - 1 - i], inlist[0]
            Sorters.bubbledown(inlist, 0, length - 2 - i)

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

    def bubblesort(mylist):

        length = len(mylist)
        for i in range(length):
            for j in range(length - 1 - i):
                if mylist[j] > mylist[j + 1]:
                    temp = mylist[j]
                    mylist[j] = mylist[j+1]
                    mylist[j+1] = temp
        return mylist
                       

