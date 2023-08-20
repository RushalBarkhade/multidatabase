
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import generics
from website.models import Article
from website.serializer import ReadDBAPISerializer,WriteDBAPISerializer
# Create your views here.


class ReadDBAPI(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReadDBAPISerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        return super().get_queryset()
       


class WriteDBAPI(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request):
        print(request.data)
        serializer = WriteDBAPISerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        