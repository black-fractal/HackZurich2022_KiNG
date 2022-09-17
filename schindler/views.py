from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from schindler.api.lift import lifts_info


def dashboard(request):
    return redirect('schindler-lifts')


def lifts_view(request):
    return render(request, 'schindler/lifts.html')


@csrf_exempt
def lifts_api(request):
    return JsonResponse(lifts_info(), safe=False)
