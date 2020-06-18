from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    ''' test API views '''

    def get(self ,request,format=None):
        ''' returns a list of APIview features '''
        an_apiview = [
        'Uses HTTP methods as functions(get,post,patch,put,delete)',
        'Is similar to a traditional Django views',
        'Gives you the most control over your application logic ',
        'Is mapped manually to URLs',
        'hellooooo',

        ]
        return Response({"massage":"Hello!",'an_apiview':an_apiview})   ### json syntax
