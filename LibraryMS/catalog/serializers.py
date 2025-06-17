from catalog.models import Book
from rest_framework import serializers



class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    summary = serializers.CharField(max_length=225)