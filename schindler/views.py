from django.http import JsonResponse
from django.shortcuts import render

from schindler.api.lift import lifts_info


def dashboard(request):
    pass


def lifts_view(request):
    return render(request, 'schindler/lifts.html')


def lifts_api(request):
    return JsonResponse(lifts_info(), safe=False)
