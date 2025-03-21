from django.contrib import admin
from .models import Portfolio
# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'context', 'img']}),
    ]

admin.site.register(Portfolio, PortfolioAdmin)