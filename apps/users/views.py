from django.http import JsonResponse


from .models import User
# 这个 ArticleListSerializer 暂时还没有
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from users.serializers import ProfileSerializer


# Create your views here.


# 视图函数
# @api_view(['GET'])
class UserProfileView(APIView):
    def get(self, request, format=None):
        user = User.objects.get(id=1)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, format=None):
        user = request.user
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)