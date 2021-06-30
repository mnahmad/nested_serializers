from django.shortcuts import render


# for this code 
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book # just to check if I can import models 

from .serializers import BookSerializer, BookDetailsSerializer


from rest_framework import status # for HTTP_200_BAD_REQUES etc


class BookView(APIView):

    def post(self,request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# curl -d '{"title":"Djano cool","author":"me","rbook":[{"summary":"Best book ever"}]}'  -X POST http://127.0.0.1:8000/add/

# curl --header "Content-Type: application/json" --request POST --data '{"title":"Djano cool","author":"me","rbook":[{"summary":"Best book ever"}]}' http://127.0.0.1:8000/add/
  