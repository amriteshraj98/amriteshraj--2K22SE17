from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Recognition, Endorsement, Redemption

# Customizing the User admin interface
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_total_credits')
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Method to display total credits in the admin panel
    def get_total_credits(self, obj):
        total_credits = Recognition.objects.filter(sender=obj).aggregate(models.Sum('credits'))['credits__sum'] or 0
        return total_credits

    get_total_credits.short_description = 'Total Credits'

# Register the custom User model in the admin panel
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Admin interface for Recognition
class RecognitionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'credits', 'timestamp')
    search_fields = ('sender__username', 'receiver__username')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

# Admin interface for Endorsement
class EndorsementAdmin(admin.ModelAdmin):
    list_display = ('recognition', 'endorser', 'timestamp')
    search_fields = ('endorser__username',)
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

# Admin interface for Redemption
class RedemptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'credits_redeemed', 'voucher_value', 'timestamp')
    search_fields = ('user__username',)
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

# Register models with the admin interface
admin.site.register(Recognition, RecognitionAdmin)
admin.site.register(Endorsement, EndorsementAdmin)
admin.site.register(Redemption, RedemptionAdmin)
