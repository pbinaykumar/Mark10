from django.contrib import admin

from .models import Chat,Connection_Room

admin.site.register(Chat)



class Connection_Room_Admin(admin.ModelAdmin):
    list_display = ['id','user1','user2','connection_id']
    list_display_links = ['user1','user2','connection_id']
admin.site.register(Connection_Room,Connection_Room_Admin)