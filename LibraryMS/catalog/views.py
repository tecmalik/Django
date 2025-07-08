import smtplib
from gc import get_objects
from operator import index

from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import get_available_image_extensions
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Book, Author, BookImage, BookInstance
from .serializers import BookSerializer, AuthorSerializer, AddBookSerializer, BookImageSerializer, \
    BookInstanceSerializer


# Create your views here.

# @api_view()
# def get_books(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     # return HttpResponse("Hello, world. You're at the books page.")
#     return Response(serializer.data, status=status.HTTP_200_OK )
#
# @api_view()
# def get_authors(request):
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK )
#
#
# @api_view(['Get'])
# def update_author(request, pk):
#     author = Author.objects.get(pk=pk)
#     serializer = AuthorSerializer(author, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# @api_view(['post'])
# def add_author(request):
#     author = AuthorSerializer(data=request.data)
#     author.is_valid(raise_exception=True)
#     author.save()
#     return Response(author.data, status=status.HTTP_201_CREATED)
#
# @api_view(['post'])
# def delete_author(request, pk):
#     author = Author.objects.get(pk=pk)
#     author.delete()
#     return Response(author.data, status=status.HTTP_204_NO_CONTENT)

# or all of that up there.
class AddAuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




class GetUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




def greet(request,name):
    # return HttpResponse(f"hello, {name}.")
    return render(request, 'index.html',{'name':name})


@api_view(['GET'])
def image_details(request, pk):
    book_image = get_object_or_404(Book, id=pk)
    serializer = BookImageSerializer(book_image)
    return Response(serializer.data, status=status.HTTP_200_OK)


# combining both 51 and 58 will be vew set(generating the url dynamically
#all crud it works with rout not urls
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBookSerializer
        elif self.request.method == 'GET':
            return AddBookSerializer
        return BookSerializer

class BookImageViewSet(viewsets.ModelViewSet):
    queryset = BookImage.objects.all()
    serializer_class = BookImageSerializer

    def perform_create(self, serializer):
        # print("KWARGS IN PERFORM_CREATE:",self.kwargs)
        book_id = serializer.data['book_pk']
        if not book_id:
            raise ValueError("Book_id missing in kwargs!")
        serializer.save(book_id=book_id)


@permission_classes(IsAuthenticated)
@api_view(['POST'])
def borrow_book(request, pk):
    # Book.objects.filter(pk=pk) #or use the method from django shortcut
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    data = BookInstanceSerializer(data=request.data)
    data.is_valid(raise_exception=True)
    BookInstance.objects.create(
        user = user,
        book=book,
        comments = data.validated_data['comments'],
        return_date = data.validated_data['return_date']
    )
    # book_instance = BookInstance()
    # book_instance.user = user
    # book_instance.book = book
    # book_instance.return_date = data.validated_data['return_date']
    # book_instance.comments = data.validated_data['comments']
    # book_instance.save()
    subject = "Notification from library MS"
    message = "Your book has been borrowed successfully"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    try :
        send_mail(subject,
                  message,
                  from_email,
                  recipient_list=recipient_list,)
    except smtplib.SMTPAuthenticationError as e:
        return Response({"message": f'{e}'} ,status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response({"message": "book borrowed successfully"},status=status.HTTP_200_OK)


class GetUpdateDeleteAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

