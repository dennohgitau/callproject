from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Mofast, Trade2w, Eglobal, Unateus, Halisi, Mainstream, Clinton, WarehouseKe, Adlat, BNE, Vital, \
    User


class MofastAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date', 'total', 'scheduled', 'percentage')
    search_fields = ('owner__username', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class TradeAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class EglobalAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class UnateusAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class HalisiAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class MainstreamAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class ClintonAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class WarehouseKeAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class AdlatAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class BNEAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


class VitalAdmin(admin.ModelAdmin):
    list_display = ('owner',  'date', 'scheduled', 'percentage')
    search_fields = ('owner', 'date')
    list_per_page = 10
    list_filter = ('owner', 'date')
    ordering = ('-date',)


admin.site.register(Mofast, MofastAdmin)
admin.site.register(Trade2w, TradeAdmin)
admin.site.register(Eglobal, EglobalAdmin)
admin.site.register(Unateus, UnateusAdmin)
admin.site.register(Halisi, HalisiAdmin)
admin.site.register(Mainstream, MainstreamAdmin)
admin.site.register(Clinton, ClintonAdmin)
admin.site.register(WarehouseKe, WarehouseKeAdmin)
admin.site.register(Adlat, AdlatAdmin)
admin.site.register(BNE, BNEAdmin)
admin.site.register(Vital, VitalAdmin)


