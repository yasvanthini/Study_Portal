from django.contrib import admin
from .models import (
    Category,
    Amenity,
    Listing,
    Image,
    HouseRent,
    Job,
    Service,
    Service_Amenity,
    Skill,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)


class AmenityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name", "description")


admin.site.register(Skill, SkillAdmin)
admin.site.register(Job)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Listing)
admin.site.register(Image)
admin.site.register(HouseRent)
admin.site.register(Service_Amenity)
