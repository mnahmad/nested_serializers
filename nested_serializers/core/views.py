from django.shortcuts import render


# for this code 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


from rest_framework.parsers import MultiPartParser, FormParser  # for photo uploader

from .models import Book, country, state, town, MyPhoto, Entry, One2Many,person

from .serializers import BookSerializer,CountrySerializer, MyPhotoSerializer, PersonSerializer


from rest_framework import status # for HTTP_200_BAD_REQUES etc

import json # to creat JSON object for One2Many serializer

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

class MyPhotoView(APIView):

    parser_class = (MultiPartParser,FormParser)

    def post(self,request):

        file_serializer = MyPhotoSerializer(data=request.data)
        print(file_serializer)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class One2ManyView(APIView):

    def post(self,request):
        try:
            data_json = request.data

            entry_json = data_json
            print(entry_json)
            
            entry_json.pop('id')

            print(entry_json)
            one2many_json = entry_json.pop('one2many') 
            print(entry_json)
            
            entry_obj = Entry.objects.create(**entry_json)

            print(one2many_json)

            option_str = ''
            for option in one2many_json:
                print(option)
                option_str +=option +" "

            print(option_str)  
            option_json_str = {}  # create dictionary
            option_json_str['option'] = option_str  # append dictionary 
            option_json = json.dumps(option_json_str)   # convert dictonrary to json like str
            option_json = json.loads(option_json)       # convert json str to json obj 

            #option_json = serializers.Serializer ('json',option_json)

            print(option_json)


            One2Many.objects.create(**option_json,entry=entry_obj)
            

            return Response(status=status.HTTP_200_OK)
            
        except Exception as e:
            #return Response(e, status=status.HTTP_400_BAD_REQUEST)    
            return Response(data={"error": str(e)},status=status.HTTP_400_BAD_REQUEST)





class PersonView(APIView):
    """
    This class shows an exmaple to change JSON key name according to the serializer/model field name
    """
    
    def post(self, request):

        data_json = request.data

        entry_json = data_json
        print(entry_json)
    
        
        # rename JSON key 'name' to 'first_name'
        entry_json['first_name'] = entry_json.pop('name')
        
        print(entry_json)

        person.objects.create(**entry_json)
        
    
        return Response(status=status.HTTP_200_OK)
