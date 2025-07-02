from catalog.models import Book
from rest_framework import serializers

from user.models import Author




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','summary', 'author']

        author = serializers.ManyRelatedField(
            Author.objects.all(),
            read_only=True)

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # summary = serializers.CharField(max_length=225)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name','last_name','email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id','title','summary', 'author']