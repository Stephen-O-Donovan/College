
def merge_bottom_up(mylist):

    length = len(mylist)
    array_list = [None]*length
    
    for i in range(length):
        array_list[i] = [mylist[i]]
        
    while len(array_list) > 1:
        array_list = _merge_bottom_up(array_list)
        
    print(array_list[0])
    return (array_list[0])

def _merge_bottom_up(array_list):
    
    
    length = len(array_list)
    result = [None]*length
    i = 0
    
    while i < length//2:
        
        left = array_list[i*2]
        right = array_list[i*2 + 1]
        j = 0
        k = 0
        m = 0
        #temp_list = []
        
        while j < len(left) and k < len(right):
            print(m)
            if left[j] < right[k]:
                result[m] = left[j]
                result[m+1] = right[k]
                #temp_list.append(left[j])
                j += 1
                m += 1
            else:
                #temp_list.append(right[k])
                result[m] = right[k]
                result[m+1] = left[j]
                k += 1
                m += 1
                
            print(result)
            
                
                
        #temp_list.extend(left[j:])
        #temp_list.extend(right[k:])
        #result.append(temp_list)

        i += 1
        
    if length % 2 == 1:
        result.append(array_list[-1])
        
    return result

def check(testlist):

    i = 0
    end = len(testlist) - 1
    errors = False
    while i < end and errors == False:
        if testlist[i] > testlist[i+1]:
            print(testlist[i])
            print(testlist[i+1])
            errors = True
            break
        i += 1

    if errors:
        print('Error')
    else:
        print('All good')

thelist = [4,3,6,2,7,9, 11, 16, 23, 12, 5, 19]
merge_bottom_up(thelist)
check(merge_bottom_up(thelist))
