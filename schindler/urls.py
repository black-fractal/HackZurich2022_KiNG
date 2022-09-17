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

    # clustering
    # path('schindler/cluster/', cluster, name='schindler-cluster'),
    # path('schindler/cluster/image/', cluster, name='schindler-cluster-image'),

    # simulation
    path('schindler/simulation/generate/', generate_simulation_api, name='schindler-simulation-generate'),
    path('schindler/simulation/run/', run_simulation, name='schindler-simulation-run'),
    path('schindler/simulation/stop/', stop_simulation, name='schindler-simulation-stop'),

    path('schindler/simulation/', list_simulation, name='schindler-simulation'),

    path('schindler/simulation/', list_simulation, name='schindler-simulation'),
]
