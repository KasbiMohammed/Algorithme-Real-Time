from django.shortcuts import render
from django.http import JsonResponse
from .scheduling import Task, rm_schedule, dm_schedule, edf_schedule, llf_schedule, fcfs_schedule, sjf_schedule, create_gantt_chart
import json
import plotly

def index(request):
    return render(request, 'scheduler/index.html')

def simulate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tasks = []
        for task_data in data['tasks']:
            task = Task(
                id=task_data['id'],
                period=task_data['period'],
                execution_time=task_data['execution_time'],
                deadline=task_data['deadline'],
                arrival_time=task_data['arrival_time']
            )
            tasks.append(task)
        
        simulation_time = data['simulation_time']
        algorithm = data['algorithm']
        
        if algorithm == 'rm':
            timeline = rm_schedule(tasks, simulation_time)
            title = "Rate Monotonic (RM) Scheduling"
        elif algorithm == 'dm':
            timeline = dm_schedule(tasks, simulation_time)
            title = "Deadline Monotonic (DM) Scheduling"
        elif algorithm == 'edf':
            timeline = edf_schedule(tasks, simulation_time)
            title = "Earliest Deadline First (EDF) Scheduling"
        elif algorithm == 'llf':
            timeline = llf_schedule(tasks, simulation_time)
            title = "Least Laxity First (LLF) Scheduling"
        elif algorithm == 'fcfs':
            timeline = fcfs_schedule(tasks, simulation_time)
            title = "First Come First Served (FCFS) Scheduling"
        elif algorithm == 'sjf':
            timeline = sjf_schedule(tasks, simulation_time)
            title = "Shortest Job First (SJF) Scheduling"
        
        fig = create_gantt_chart(timeline, tasks, title)
        gantt_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        
        return JsonResponse({
            'gantt_data': gantt_json,
            'timeline': timeline
        })
