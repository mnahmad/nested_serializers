from rest_framework import serializers
from .models import Book,BookDetails


class BookDetailsSerializer(serializers.ModelSerializer):
    summary = serializers.CharField(max_length=23)

    class Meta:
        model = BookDetails
        fields= ('id','summary')



class BookSerializer(serializers.ModelSerializer):
    rbook = BookDetailsSerializer(many=True)

    def create(self,validated_data):
        temp_book_details = validated_data.pop('rbook')
        
        # Check if books exists (aka record exists in parent table)    
        book_title = validated_data.pop('title')
        if not Book.objects.filter(title=book_title).exists():
            book = Book.objects.create(**validated_data)
        else:
            book = Book.objects.get(title=book_title)

        for i in temp_book_details:
            #BookDetails.objects.create(**i,bok=new_book)     
            BookDetails.objects.create(**i,bok=book)
            
        return book     

    class Meta:
        model = Book
        fields = ('id','rbook','title','author')   

