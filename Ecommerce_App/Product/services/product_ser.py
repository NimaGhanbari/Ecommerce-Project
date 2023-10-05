# REST Framework
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

# Local
from Ecommerce_App.PostFiles.models import Post_File


def Filtering(request, products):
    brand = request.GET.get('brand')
    price_max = request.GET.get('price_max')
    price_min = request.GET.get('price_min')
    is_enable = request.GET.get('is_enable')

    if brand:
        try:
            products = products.filter(categories=brand)
        except Exception as ex:
            return Response({f"detail": "category is not valid - {ex}"}, status=status.HTTP_400_BAD_REQUEST)
    if price_max or price_min:
        # temp = []
        # for product in products:
        #    if product.price > price_min and product.price < price_max:
        #        temp.append(product)
        # products = temp

        # products = list(filter(lambda product: product.get(
        #    'price') > price_min and product.get('price') < price_max, products))
        if price_max == None or price_max == None:
            return Response({"detail": "price min or price max is not valid"}, status=status.HTTP_400_BAD_REQUEST)

        products = products.filter(price__range=[price_min, price_max])

        # return Response({f"detail": "price is not valid - {ex}"}, status=status.HTTP_400_BAD_REQUEST)
    # if new:
    #    products = Sort_By(products,by=4)
    if is_enable:
        try:
            # products = list(
            #    filter(lambda product: product.get('is_enable') == True, products))
            products = products.filter(is_enable=True)
        except Exception as ex:
            return Response({f"detail": "price is not valid - {ex}"}, status=status.HTTP_400_BAD_REQUEST)

    return products


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = Post_File
        fields = ('title', 'fil', 'file_type')

    def get_file_type(self, obj):
        return obj.get_file_type_display()


def bubblesort(elements):
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i].created_at < elements[i + 1].created_at:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements


def selectionSortP(elements):
    size = len(elements)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if elements[j].count_reactions['popular'] > elements[min_index].count_reactions['popular']:
                min_index = j
                # swapping the elements to sort the array
        elements[ind], elements[min_index] = elements[min_index], elements[ind]
    return elements


def selectionSort(elements, id):
    size = len(elements)
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
        (elements[ind], elements[min_index]) = (
            elements[min_index], elements[ind])
    return elements


def Sort_By(elements, by=4):
    # 0:محبوبترین
    # 1:پرفروشترین
    # 2:گرانترین
    # 3:ارزانترین
    # 4:جدیدترین
    if by == 0:
        return selectionSortP(elements=elements)
    elif by == 1:
        pass
    elif by == 2:
        return selectionSort(elements=elements, id=by)
    elif by == 3:
        return selectionSort(elements=elements, id=by)
    elif by == 4:
        return bubblesort(elements=elements)


def Ordering(request, products):
    new = request.GET.get('new')
    popular = request.GET.get('popular')
    # most visited
    # best seller
    Inexpensive = request.GET.get('Inexpensive')
    Expensive = request.GET.get('Expensive')

    if new:
        return Sort_By(list(products), 4)
    if popular:
        return Sort_By(list(products), 0)
    if Inexpensive:
        return Sort_By(list(products), 3)
    if Expensive:
        return Sort_By(list(products), 2)

    return products
