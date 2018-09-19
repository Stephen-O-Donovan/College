class Sorters():

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
                _quicksort(mylist, first, b - 1)
                _quicksort(mylist, b + 1, last)
