from django.contrib import admin

from .models import storeItems,Specs,CartItem

class itemsAdmin(admin.ModelAdmin):
    list_display = ('name','sku','dateAdded',)
    search_fields = ('name','sku')
    list_filter = ('dateAdded','sku')
    ordering = ('dateAdded',)

class specsAdmin(admin.ModelAdmin):
     list_display = ('title','item')
     search_fields = ('item__sku','title')

admin.site.register(storeItems,itemsAdmin)
admin.site.register(Specs,specsAdmin)
admin.site.register(CartItem)