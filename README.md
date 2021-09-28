# Nested Serializer 
Nested serializers is a difficult concept and it took me a lot of time to figure out all the issues, thus, I decided to create a workiing example so others can also reading the stated blogs plus go through here. This repo also contains example code to allow image upload using DRF, please see the section [Photo Upload](#Photo-upload). Since I am using the repo as test bed, so a specific case (where JSON contain data in a specific format) is also tested in section [One2Many JSON](One2Many-JSON).  

Most of the code in this repo is taken from [this](https://medium.com/@rushic24/creating-nested-serializers-in-django-rest-framework-5110c6674fba) medium post and [this](https://medium.com/@gurupratap.matharu/build-a-restapi-using-nested-serializers-in-django-rest-framework-c0f6a31fd865) medium post.  The code is enhanced to apply some chesk, explained in details below. 

How this repo should be used. 
1. Read [this](https://medium.com/@rushic24/creating-nested-serializers-in-django-rest-framework-5110c6674fba) post first and then [this](https://medium.com/@gurupratap.matharu/build-a-restapi-using-nested-serializers-in-django-rest-framework-c0f6a31fd865).

2. Clone this repository
3. create virtual env
4. Install packages as required by this repo and explained below
5. Run `python3 manage.py makemigratiojns` and `python3 manage.py mightate`
6. Add `SECRET_KEY ` to settings.py
7. Run `python3 manage.py runserver`

4. Packages required

```
Django==2.2.16
djangorestframework==3.12.2
```


The JSON used is as follows

```
{
    "test":"test",
    "country": {
      "cntry_name": "Pakistan",
      "currency": "PKR"
    },
    "state": {
      "state_name": "Punjab"
    },
    "town": {  
      "town_name": "rawalpindi"
    }
}

```

Note, I am using postman, however one can use curl as well. For culr, use the following command 

```
curl --header "Content-Type: application/json" --request POST --data '{"test":"test","country": {"cntry_name": "Kenya","currency": "Ksh"},"state": {"state":"Nairobi"},"town": {"town_name": "cbd"}}' http://127.0.0.1:8000/addtown/

```

## Photo upload
Photo upload using DRS 

Code taken from [this blog](https://chrisbartos.com/articles/uploading-images-drf/) 

how to use the code. 

1. make changes in the setting.py for media file. 
2. add class in models to take care of the photo data 
3. add a serializer to handle the data. 
4. follow the blog to build post request 


## One2Many JSON

The JSON in question is 

```JSON

[
  {
    "entry":{
     "id": 1,
     "recorded_date": "2021-9-27",
     "name":"David",
     "description": "Description of the record",
     "one2many":[
      "one",
      "two",
      "three"  
     ] 

    }
  }

]

```


## Some commands related to Sqlite

Connect with your database using CLI

```
Sqlite3 db.sqlite3 
```

How to see all tables

```
.tables
```

How to see table structure

```
.schema tablename
```




