from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["name","email"]
    search_fields = ["name"]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber,SubscriberAdmin)