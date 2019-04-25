from django.contrib import admin

from . import models


class KidAdmin(admin.ModelAdmin):
    pass


class ParentAdmin(admin.ModelAdmin):
    pass


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', )


class LevelAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(models.Kid, KidAdmin)
admin.site.register(models.Parent, ParentAdmin)
admin.site.register(models.Plan, PlanAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Level, LevelAdmin)
