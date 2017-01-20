from django.contrib import admin

from .models import Dpl, WeldNumber

# Register your models here.


class WeldNumberAdmin(admin.ModelAdmin):
    list_display = ('weld_number', 'dpl', 'xray_status', 'qc_person')
    list_editable = ('xray_status',)
    list_filter = ('dpl', 'xray_status', 'qc_person',
                   'created', 'xray_completed')
    ordering = ('xray_status', 'created')
    fieldsets = (
        (None, {
            'fields': ('qc_person', 'weld_number', 'dpl', 'xray_status',
                       'status')
        }),
        ('Additional Notes', {
            'fields': ('weld_notes',),
            'classes': ('collapse',),
        })
    )


class DplAdmin(admin.ModelAdmin):
    list_display = ('dpl_number', 'pipe_size', 'wall_size')
    list_filter = ('pipe_size', 'wall_size')
    search_fields = ('dpl_number',)

admin.site.register(WeldNumber, WeldNumberAdmin)
admin.site.register(Dpl, DplAdmin)
