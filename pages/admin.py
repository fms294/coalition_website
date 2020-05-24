from django.contrib import admin

# Register your models here.
from .models import Feedback, Membership

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
    list_filter = ('date',)
    search_fields = ('firstname','lastname','email')

    class Meta:
        model=Feedback

admin.site.register(Feedback, FeedbackAdmin)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone_number', 'country')
    list_filter = ('date','country')
    search_fields = ('firstname', 'lastname', 'email','country')

    class Meta:
        model = Membership


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Membership,MembershipAdmin)