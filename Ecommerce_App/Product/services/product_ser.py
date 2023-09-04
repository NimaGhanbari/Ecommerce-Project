
def bubblesort(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i].created_at > elements[i + 1].created_at:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                
    return elements


def selectionSort(elements,id):
    size =len(elements)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if id == 2:
                if elements[j].price > elements[min_index].price:
                    min_index = j
            else:
                if elements[j].price < elements[min_index].price:
                    min_index = j
        # swapping the elements to sort the array
        (elements[ind], elements[min_index]) = (elements[min_index], elements[ind])
    return elements

def Sort_By(elements,by=4):
    #0:محبوبترین
    #1:پرفروشترین
    #2:گرانترین
    #3:ارزانترین
    #4:جدیدترین
    if by == 0:
        pass
    elif by == 1:
        pass
    elif by ==2:
        selectionSort(elements=elements,id=by)
    elif by ==3:
        selectionSort(elements=elements,id=by)
    elif by == 4:
        elements = bubblesort(elements=elements)
        for x in elements:
            print(x.created_at)
        return elements