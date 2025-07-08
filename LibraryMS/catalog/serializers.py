from catalog.models import Book, BookImage, BookInstance
from rest_framework import serializers

from catalog.models import Book , Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','first_name','last_name', 'email', 'dob']



class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    # images = serializers.StringRelatedField(many=True, read_only=True)
    images = serializers.HyperlinkedRelatedField(
        view_name='book-image-detail',
        queryset=BookImage.objects.all(),
        many=True
    )
    class Meta:
        model = Book
        fields = ['id', 'title', 'summary' ,'images', 'author']


class AddBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn' , 'summary' ]


class BookImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book_id = self.context['book_id']
        return BookImage.objects.create(book_id=book_id, **validated_data)

    class Meta:
        model = BookImage
        fields = ['id', 'image']

class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['return_date','comments']


# ///nb djoser google search for jwt