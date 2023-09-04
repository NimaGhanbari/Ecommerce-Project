from Ecommerce_App.Category.models import Category


def is_subcategory(categor):
    return Category.objects.filter(parent=categor)
    
    
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
        pass
    elif by ==3:
        pass
    elif by == 4:
        def bubblesort(elements):
            # Looping from size of array from last index[-1] to index [0]
            for n in range(len(elements)-1, 0, -1):
                for i in range(n):
                    if elements[i].created_at > elements[i + 1].created_at:
                        swapped = True
                        # swapping data if the element is less than next element in the array
                        elements[i], elements[i + 1] = elements[i + 1], elements[i]
            
            for x in elements:
                print(x.created_at)
            return elements