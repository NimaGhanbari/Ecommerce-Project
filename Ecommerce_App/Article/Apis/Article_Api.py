

# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from Ecommerce_App.Article.models import Article

from datetime import datetime


class Article_view(APIView):

    class OutPutSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = ("title", "cover", "slug", "uniqe_code")

    def get(self, request, count):
        # There is no need to check the received number because this function is supposed to display 5 or all articles.
        if count == 5:
            return Response(self.OutPutSerializer(Article.objects.filter(created_at__lte=datetime.now()).order_by('-created_at')[:count], many=True, context={"request": request}).data)
        else:
            return Response(self.OutPutSerializer(Article.objects.filter(created_at__lte=datetime.now()).order_by('-created_at'), many=True, context={"request": request}).data)


class Article_Detail_View(APIView):

    class OutPutSerializer(serializers.ModelSerializer):

        class Meta:
            model = Article
            fields = ("__all__")

    def get(self, request, aslug):
        return Response(self.OutPutSerializer(Article.objects.filter(slug=aslug,is_active=True), many=True, context={"request": request}).data)
