from django.contrib import admin
from myapp.models import Page,Post,Song

# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_anme','page_cat','page_publish_date','user']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title','post_cat','pots_publish_date','user']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name','song_dur','written_by']
