from django.contrib import admin
from .models import Book,BookRecord

class BookDiplay(admin.ModelAdmin):
    list_display=['Tittle','ISBN','PublicationYear','Author','Available']
    list_display_links=['Tittle','ISBN','PublicationYear','Author']
    list_editable=['Available']
    search_fields=['Tittle']
    list_filter=['Available']

class BookRecordDisplay(admin.ModelAdmin):
    list_display=[ 'book_title','user_email','Took_On','Return_On']
    search_fields=['book_title']

admin.site.register(Book, BookDiplay)
admin.site.register(BookRecord,BookRecordDisplay)








