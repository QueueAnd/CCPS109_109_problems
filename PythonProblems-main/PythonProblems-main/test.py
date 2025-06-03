def arithmetic_progression(items):
    max_start=items[0]
    max_length=2
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            stride = items[j] - items[i]
            length=2 #initial lenght for each loop
            previous_item=items[j] #initialize the start for each loop
            for k in range(j+1, len(items)):
                if items[k]-previous_item==stride:
                    length = length +1
                    previous_item=items[k] #update the current item to compare with the next item
            if length > max_length:
                max_start=items[i] #update the maximum length and its start and stride
                max_length=length
                max_stride=stride
            if length >= len(items) -i:
                return(max_start,max_stride,max_length) # stop when the best possible result is found.
    return(max_start,max_stride,max_length) # return in normal way

#print(arithmetic_progression([2, 4, 6, 7, 8, 12, 17]))
#print(arithmetic_progression([1, 2, 36, 49, 50, 70, 75, 98, 104, 138, 146, 148, 172, 206, 221, 240, 274, 294, 367, 440]))
print(arithmetic_progression(range(1000000)))

#print(arithmetic_progression([2, 3, 7, 20, 25, 26, 28, 30, 32, 34, 36, 41, 53, 57, 73, 89, 94, 103, 105, 121, 137, 181, 186, 268, 278, 355, 370, 442, 462, 529, 554, 616, 646, 703]))