from django.contrib import admin

from .models import Feedback


class FeedAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'phone',
        'email',
        'name',
        'message'
        )


admin.site.register(Feedback, FeedAdmin)