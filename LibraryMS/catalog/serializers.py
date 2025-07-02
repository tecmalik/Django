from catalog.models import Book
from rest_framework import serializers

from user.models import Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','summary']