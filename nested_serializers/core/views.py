from django.shortcuts import render


# for this code 
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book, country, state, town

from .serializers import BookSerializer, BookDetailsSerializer, StateSerializer,CountrySerializer


from rest_framework import status # for HTTP_200_BAD_REQUES etc


class BookView(APIView):

    def post(self,request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class StateView(APIView):

    def post(self,request):
        
        c = request.data.pop('country') # I need it at 2 places, since pop can only work once on a list, thus, I am saving in variable 
        serializer = CountrySerializer(data=c, required=False)

        if serializer.is_valid():
            #serializer.save()

            #c = request.data.pop('country')
            s = request.data.pop('state')

            cntry = country.objects.create(**c)
            state.objects.create(**s,country=cntry)



            return Response(serializer.data,status=status.HTTP_200_OK)
            #return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
        #return Response(status=status.HTTP_400_BAD_REQUEST)    



class TownView(APIView):

    def post(self,request):

        """
        Note: the line below has 2 purposes
        1. to validate the country part of json and pass the check
        2. to help in creating country object if not exists

        """
        country_json = request.data.pop('country') 

        # Now create country serialise 
        cntrySerializer = CountrySerializer(data=country_json) 

        if cntrySerializer.is_valid():

            country_name = country_json['cntry_name']
            if not country.objects.filter(cntry_name=country_name).exists():    
                country_obj = country.objects.create(**country_json)
            else:
                country_obj = country.objects.get(cntry_name=country_name)


            state_json =  request.data.pop('state')
            state_name = state_json['state_name']
            if not state.objects.filter(state_name=state_name).exists():
                state_obj = state.objects.create(**state_json,country=country_obj)
            else:
                state_obj = state.objects.get(state_name=state_name)    

            town_json = request.data.pop('town')
            town_name = town_json['town_name']
            if not town.objects.filter(town_name=town_name).exists():
                town_obj = town.objects.create(**town_json,state=state_obj)
            else:
                town_obj = town.objects.get(town_name=town_name)    


            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)    
