import random

def partial(mylist, p):

    partial_list = mylist
    n = len(mylist)
    for _i in range (p):
        j = random.randint(0, n-1)
        k = random.randint(0, n-1)
        while k == j:
            k = random.randint(0, n-1)
        #temp = partial_list[j]
        #partial_list[j] = partial_list[l]
        partial_list[j], partial_list[k] = partial_list[k], partial_list[j]
        print(partial_list)
    #return partial_list

mylist = [0, 1, 2, 3, 4, 5 , 6, 7, 8]
partial(mylist, 3)
