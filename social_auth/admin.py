from django.contrib import admin
from .models import *



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slag','content','date','tags',)
    list_filter = ('date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slag': ('title',)}
   


admin.site.register(Post,PostAdmin)

