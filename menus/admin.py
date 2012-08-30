from django.contrib import admin
from menus.models import Menu, Plato, Excepcion

class PlatoInline(admin.TabularInline):
    model = Plato
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titulo del menu',               {'fields': ['titulo']}),
        ('Fecha del Menu', {'fields': ['fecha']}),
    ]
    inlines = [PlatoInline]
    list_display = ('titulo', 'fecha')
    list_filter = ['fecha']
    date_hierarchy = 'fecha'
admin.site.register(Menu, MenuAdmin)

class ExcepcionInline(admin.TabularInline):
    model = Excepcion
    extra = 1

class PlatoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre',               {'fields': ['titulo']}),
        ('Tipo de plato', {'fields': ['tipo']}),
    ]
    inlines = [ExcepcionInline]
    #list_display = ('titulo', 'fecha')
    #list_filter = ['fecha']
    #date_hierarchy = 'fecha'
admin.site.register(Plato, PlatoAdmin)

class ExcepcionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre',               {'fields': ['descripcion']}),
    ]
admin.site.register(Excepcion, ExcepcionAdmin)