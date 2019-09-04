from django.db import models

class Author(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=20)
	subject=models.CharField(max_length=20)

	def __str__(self):
		return self.first_name

class Book(models.Model):
	title=models.CharField(max_length=30)
	author=models.ForeignKey(Author,related_name='authorbookpage',on_delete=models.CASCADE)
	released_date=models.DateField()
	rating=models.IntegerField()

	def __str__(self):
		return self.title