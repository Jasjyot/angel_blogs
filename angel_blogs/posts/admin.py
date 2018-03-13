from django.contrib import admin
from .models import Post
# Register your models here.



#model admin options
#customizing admin pannel

class PostModelAdmin(admin.ModelAdmin):
    list_display=["title","updated","timestamp"]
    #list_display_links=["updated"]
    #list_editable=["publish date and time can be edited according to one's need "]
    list_filter=["updated" , "timestamp"]
    search_fields=["title","content"]
    class Meta:
        model=Post

admin.site.register( Post, PostModelAdmin )


