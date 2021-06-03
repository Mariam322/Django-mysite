from django.contrib import admin
from Bibliotheque.models import Genre,AuthorAdmin,Author

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)

admin.site.register(Author,AuthorAdmin)


