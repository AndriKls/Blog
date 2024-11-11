from django.contrib import admin
from blog.models import Post, Author, Tag 

# Register your models here.


class PostAdmin(admin.ModelAdmin):
   prepopulated_fields = {"slug": ("title",)}
   list_filter = ("author", "Date")
   list_display = ("title", "author", "Date")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
