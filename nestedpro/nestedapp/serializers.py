from rest_framework.serializers import ModelSerializer

from .models import Author,Book


class BookSerializer(ModelSerializer): #give preference first to Bookseriailizer
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
	authorbookpage=BookSerializer(many=True, read_only=True) #add these line for nested serializer effect
	class Meta:
		model = Author
		fields = '__all__'

