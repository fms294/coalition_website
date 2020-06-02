from django.contrib import admin

# Register your models here.
from .models import Feedback, Membership

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'message', 'date')
    list_filter = ('date',)
    search_fields = ('prenom','nom','email')

    class Meta:
        model=Feedback



class MembershipAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'areacode', 'phone_number', 'country','date')
    list_filter = ('date','country')
    search_fields = ('firstname', 'lastname', 'email','country')

    class Meta:
        model = Membership


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Membership,MembershipAdmin)