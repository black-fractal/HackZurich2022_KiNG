from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from schindler.api.lift import lifts_info
from schindler.api.users import generate_random_users
from schindler.models import UserProfile


def dashboard(request):
    return redirect('schindler-lifts')


def lifts_view(request):
    return render(request, 'schindler/lifts.html')


@csrf_exempt
def lifts_api(request):
    try:
        return JsonResponse(lifts_info(), safe=False)
    except:
        return HttpResponse('Error: Could not fetch data')


@csrf_exempt
def generate_users_api(request):
    if request.method == "POST":
        try:
            number = int(request.POST.get("users", "0"))
            return JsonResponse(generate_random_users(number), safe=False)
        except:
            return HttpResponse('Error: Could not generate random users')


@csrf_exempt
def list_users(request):
    users = UserProfile.objects.all()
    return render(request, 'schindler/users.html', {'users': users})
