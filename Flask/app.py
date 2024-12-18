from flask import Flask, render_template, request, jsonify
from scheduling import Task, rm_schedule, dm_schedule, edf_schedule, llf_schedule, fcfs_schedule, sjf_schedule, create_gantt_chart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
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
    return jsonify({
        'gantt_data': fig.to_json(),
        'timeline': timeline
    })

if __name__ == '__main__':
    app.run(debug=True)
