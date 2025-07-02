from operator import index

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Create your views here.

@api_view()
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    # return HttpResponse("Hello, world. You're at the books page.")
    return Response(serializer.data, status=status.HTTP_200_OK )

def greet(request,name):
    # return HttpResponse(f"hello, {name}.")
    return render(request, 'index.html',{'name':name})
