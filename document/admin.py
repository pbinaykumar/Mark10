from django.contrib import admin
from .models import All_Format,Available_Format,Output_Format,Document,File_Type

admin.site.register(All_Format)
admin.site.register(Output_Format)

class OutputInlinee(admin.StackedInline):
    model = Output_Format


class Available_FormatAdmin(admin.ModelAdmin):
    list_display = ['id','input']
    list_display_links = ['id','input']
    inlines = [OutputInlinee]

admin.site.register(Available_Format,Available_FormatAdmin)
admin.site.register(File_Type)
admin.site.register(Document)


