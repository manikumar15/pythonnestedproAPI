from django.contrib import admin
from .models import Author,Book
admin.site.site_header = 'Mani Kumar'


class Authoradmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','subject')
    list_filter = ('first_name',)
    search_fields = ('first_name',)

admin.site.register(Author,Authoradmin)

class Bookadmin(admin.ModelAdmin):
    list_display = ('title','author','released_date','rating')
    list_filter = ('title',)
    search_fields = ('title',)

admin.site.register(Book,Bookadmin)