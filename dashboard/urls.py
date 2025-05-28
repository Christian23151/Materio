from django.contrib import admin
from django.urls import path
from dashboard.views import dashboard_stats

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_stats, name='home'),  # Root URL
    path('stats/', dashboard_stats, name='dashboard_stats'),  # /stats/
]
