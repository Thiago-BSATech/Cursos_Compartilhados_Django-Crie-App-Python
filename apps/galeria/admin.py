from django.contrib import admin
from apps.galeria.models import Fotografia




class ListandoFotografias(admin.ModelAdmin):

    list_display = ('id', 'nome', 'legenda', 'data' ,'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ("categoria", 'usuarios',)
    list_editable = ("publicada",)


admin.site.register(Fotografia, ListandoFotografias)