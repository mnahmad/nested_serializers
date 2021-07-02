# Nested Serializer 

Most of the code in this repo is taken from [this](https://medium.com/@rushic24/creating-nested-serializers-in-django-rest-framework-5110c6674fba) medium post and [this](https://medium.com/@gurupratap.matharu/build-a-restapi-using-nested-serializers-in-django-rest-framework-c0f6a31fd865) medium post.  The code is enhanced to apply some chesk, explained in details below. 

How this repo should used. 
1. Read [this](https://medium.com/@rushic24/creating-nested-serializers-in-django-rest-framework-5110c6674fba) post first and then [this](https://medium.com/@gurupratap.matharu/build-a-restapi-using-nested-serializers-in-django-rest-framework-c0f6a31fd865).

2. Clone this repository
3. create virtual env
4. Install packages as required by this repo and explained below
5. Run `makemigratiojns` and `mightate`
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



This is work in progres 