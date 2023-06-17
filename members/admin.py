from django.contrib import admin

from members.models import Members

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")

# Register your models here.
admin.site.register(Members, MemberAdmin)

