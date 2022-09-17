from django.urls import path

from schindler.views import dashboard

urlpatterns = [
    path('schindler/', dashboard, name='schindler'),

    # lifts
    path('schindler/lifts/', dashboard, name='schindler-lifts'),
    path('schindler/lifts/api/', dashboard, name='schindler-lifts-api'),
]
