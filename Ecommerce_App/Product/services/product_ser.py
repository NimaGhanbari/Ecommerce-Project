# Django
from django.db.models import QuerySet

# REST Framework
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

# Local
from Ecommerce_App.PostFiles.models import Post_File
from Ecommerce_App.Product.models import Products
from Ecommerce_App.Category.models import Category

# This function filters by receiving the filtering details from the request and performs the filter on the products
def Filtering(request, products: QuerySet[Products]):
    brand: Category = request.GET.get('brand')
    price_max: int = request.GET.get('price_max')
    price_min: int = request.GET.get('price_min')
    is_enable: bool = request.GET.get('is_enable')
    
    if brand:
        try:
            products = products.filter(categories=brand)
        except Exception as ex:
            return Response({f"detail": "category is not valid - {ex}"}, status=status.HTTP_400_BAD_REQUEST)
    if price_max or price_min:
        if price_max == None or price_max == None:
            return Response({"detail": "price min or price max is not valid"}, status=status.HTTP_400_BAD_REQUEST)

        products = products.filter(price__range=[price_min, price_max])

    if is_enable:
        try:
            products = products.filter(is_enable=True)
        except Exception as ex:
            return Response({f"detail": "price is not valid - {ex}"}, status=status.HTTP_400_BAD_REQUEST)

    return products


# This class serializes the file model objects
class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = Post_File
        fields = ('title', 'fil', 'file_type')

    def get_file_type(self, obj):
        return obj.get_file_type_display()


def bubblesort(elements: QuerySet[Products]) -> QuerySet[Products]:
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i].created_at < elements[i + 1].created_at:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]

    return elements


def selectionSortP(elements: QuerySet[Products]) -> QuerySet[Products]:
    size: int = len(elements)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if elements[j].count_reactions['popular'] > elements[min_index].count_reactions['popular']:
                min_index = j
                # swapping the elements to sort the array
        elements[ind], elements[min_index] = elements[min_index], elements[ind]
    return elements


def selectionSort(elements: QuerySet[Products], id: int) -> QuerySet[Products]:
    size: int = len(elements)
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

# This function sorts into 5 types that are used in the "Ordering" function.
def Sort_By(elements: QuerySet[Products], by: int = 4) -> QuerySet[Products]:
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

# This function sorts into 5 types. The sort value is taken from the query param, which must be a number between 0 and 5
def Ordering(request, products: QuerySet[Products]) -> QuerySet[Products]:
    sort = request.GET.get('sort')
    if sort == '4':
        return Sort_By(list(products), 4)
    if sort == '0':
        return Sort_By(list(products), 0)
    if sort == '3':
        return Sort_By(list(products), 3)
    if sort == '2':
        return Sort_By(list(products), 2)

    return products
