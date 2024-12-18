from django.shortcuts import render
from django.http import JsonResponse
from real_time_scheduling import Task, rm_schedule, dm_schedule, fcfs_schedule, sjf_schedule, edf_schedule, llf_schedule

# Create your views here.

def schedule(request):
    if request.method == 'POST':
        data = request.POST
        tasks = [Task(**task) for task in data.getlist('tasks')]
        algorithm = data['algorithm']
        simulation_time = int(data['simulation_time'])
        timeline = []

        if algorithm == 'Rate Monotonic':
            timeline = rm_schedule(tasks, simulation_time)
        elif algorithm == 'Deadline Monotonic':
            timeline = dm_schedule(tasks, simulation_time)
        elif algorithm == 'First Come First Served':
            timeline = fcfs_schedule(tasks, simulation_time)
        elif algorithm == 'Shortest Job First':
            timeline = sjf_schedule(tasks, simulation_time)
        elif algorithm == 'Earliest Deadline First':
            timeline = edf_schedule(tasks, simulation_time)
        elif algorithm == 'Least Laxity First':
            timeline = llf_schedule(tasks, simulation_time)

        return JsonResponse({'timeline': timeline})

    return render(request, 'scheduling_app/schedule.html')
