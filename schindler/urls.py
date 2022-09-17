from django.urls import path

from schindler.views import *

urlpatterns = [
    path('schindler/', dashboard, name='schindler'),

    # lifts
    path('schindler/lifts/', lifts_view, name='schindler-lifts'),
    path('schindler/lifts/api/', lifts_api, name='schindler-lifts-api'),

    # users
    path('schindler/users/generate/', generate_users_api, name='schindler-users-generate'),
    path('schindler/users/', list_users, name='schindler-users'),
]
