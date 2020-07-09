from django.contrib import admin


from .models import Post, Category, Tag, Author

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Author)