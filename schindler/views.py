import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from HackZurich2022_KiNG import settings
from schindler.api.lift import *
from schindler.api.simulation import *
from schindler.api.users import *
from schindler.models import *


def dashboard(request):
    return render(request, 'schindler/index.html')


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


@csrf_exempt
def generate_simulation_api(request):
    if request.method == "POST":
        try:
            number = int(request.POST.get("simulation", "0"))
            return JsonResponse(generate_random_simulation(number), safe=False)
        except:
            return HttpResponse('Error: Could not generate random simulation')


@csrf_exempt
def list_simulation(request):
    simulation = Simulation.objects.all()
    return render(request, 'schindler/simulation.html', {'simulation': simulation})


def run(request):
    return render(request, 'schindler/run.html')


def run_simulation(request):
    now = datetime.datetime.now()
    if not settings.SIMULATION_STATE:  # Simulation not running
        settings.SIMULATION_STATE = True

    if settings.SIMULATION_JOB_ID is not None:  # Already have a Job ID
        job_request = Simulation.objects.get(id=settings.SIMULATION_JOB_ID)
        if now - datetime.timedelta(seconds=job_request.delay) >= settings.SIMULATION_JOB_START:
            job_request.delete()
        else:
            return JsonResponse(job_request.to_json(), safe=False)

    # Assign a job ID
    request_job = Simulation.objects.all().first()
    publish(request_job.source, request_job.destination)
    settings.SIMULATION_JOB_ID = request_job.id
    settings.SIMULATION_JOB_START = now
    return JsonResponse(request_job.to_json(), safe=False)


def stop_simulation(request):
    settings.SIMULATION_STATE = False
    settings.SIMULATION_JOB_ID = None
    settings.SIMULATION_JOB_START = None

    return HttpResponse("Job Stopped")


def platte_api(request):
    pass
# TODO:return array from users
