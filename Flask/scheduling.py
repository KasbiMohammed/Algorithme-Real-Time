import plotly.graph_objects as go
from copy import deepcopy

class Task:
    def __init__(self, id, period, execution_time, deadline, arrival_time=0):
        self.id = id
        self.period = period
        self.execution_time = execution_time
        self.deadline = deadline
        self.arrival_time = arrival_time
        self.remaining_time = execution_time
        self.next_release = arrival_time
        self.current_execution = 0
        self.is_running = False

def rm_schedule(tasks, simulation_time):
    timeline = []
    current_time = 0
    tasks = deepcopy(tasks)
    current_task = None
    
    while current_time < simulation_time:
        # Vérifier les nouvelles instances de tâches
        for task in tasks:
            if current_time >= task.next_release:
                task.remaining_time = task.execution_time
                task.current_execution = 0
                task.is_running = False
                task.next_release += task.period  # Mettre à jour la prochaine libération
        
        # Obtenir les tâches actives
        active_tasks = [task for task in tasks if task.remaining_time > 0 and current_time >= task.arrival_time]
        
        if active_tasks:
            # Trier par période (priorité RM)
            active_tasks.sort(key=lambda x: x.period)
            highest_priority_task = active_tasks[0]
            
            # Vérifier si une interruption est nécessaire
            if current_task and current_task.id != highest_priority_task.id and current_task.remaining_time > 0:
                current_task.is_running = False
            
            current_task = highest_priority_task
            current_task.is_running = True
            
            # Exécuter la tâche
            timeline.append((current_task.id, current_time, current_time + 1))
            current_task.remaining_time -= 1
            current_task.current_execution += 1
            
            # Si la tâche est terminée
            if current_task.remaining_time == 0:
                current_task = None
        else:
            timeline.append(("Idle", current_time, current_time + 1))
        
        current_time += 1
    
    return timeline

def dm_schedule(tasks, simulation_time):
    timeline = []
    current_time = 0
    tasks = deepcopy(tasks)
    current_task = None
    
    while current_time < simulation_time:
        # Vérifier les nouvelles instances de tâches
        for task in tasks:
            if current_time >= task.next_release:
                task.remaining_time = task.execution_time
                task.current_execution = 0
                task.is_running = False
        
        # Obtenir les tâches actives
        active_tasks = []
        for task in tasks:
            if current_time >= task.arrival_time and current_time >= task.next_release and task.remaining_time > 0:
                active_tasks.append(task)
        
        if active_tasks:
            # Trier par deadline (priorité DM)
            active_tasks.sort(key=lambda x: x.deadline)
            highest_priority_task = active_tasks[0]
            
            # Vérifier si une interruption est nécessaire
            if current_task and current_task.id != highest_priority_task.id and current_task.remaining_time > 0:
                current_task.is_running = False
            
            current_task = highest_priority_task
            current_task.is_running = True
            
            timeline.append((current_task.id, current_time, current_time + 1))
            current_task.remaining_time -= 1
            current_task.current_execution += 1
            
            if current_task.remaining_time == 0:
                current_task.next_release = current_time + 1 - current_task.current_execution + current_task.period
                current_task.is_running = False
                current_task = None
        else:
            timeline.append(("Idle", current_time, current_time + 1))
            current_task = None
        
        current_time += 1
    
    return timeline

def edf_schedule(tasks, simulation_time):
    timeline = []
    current_time = 0
    tasks = deepcopy(tasks)
    current_task = None
    
    while current_time < simulation_time:
        # Vérifier les nouvelles instances de tâches
        for task in tasks:
            if current_time >= task.next_release:
                task.remaining_time = task.execution_time
                task.current_execution = 0
                task.is_running = False
                task.absolute_deadline = current_time + task.deadline
        
        # Obtenir les tâches actives
        active_tasks = []
        for task in tasks:
            if current_time >= task.arrival_time and current_time >= task.next_release and task.remaining_time > 0:
                active_tasks.append(task)
        
        if active_tasks:
            # Trier par deadline absolue (priorité EDF)
            active_tasks.sort(key=lambda x: x.absolute_deadline)
            highest_priority_task = active_tasks[0]
            
            # Vérifier si une interruption est nécessaire
            if current_task and current_task.id != highest_priority_task.id and current_task.remaining_time > 0:
                current_task.is_running = False
            
            current_task = highest_priority_task
            current_task.is_running = True
            
            timeline.append((current_task.id, current_time, current_time + 1))
            current_task.remaining_time -= 1
            current_task.current_execution += 1
            
            if current_task.remaining_time == 0:
                current_task.next_release = current_time + 1 - current_task.current_execution + current_task.period
                current_task.is_running = False
                current_task = None
        else:
            timeline.append(("Idle", current_time, current_time + 1))
            current_task = None
        
        current_time += 1
    
    return timeline

def llf_schedule(tasks, simulation_time):
    timeline = []
    current_time = 0
    tasks = deepcopy(tasks)
    current_task = None
    
    while current_time < simulation_time:
        # Vérifier les nouvelles instances de tâches
        for task in tasks:
            if current_time >= task.next_release:
                task.remaining_time = task.execution_time
                task.current_execution = 0
                task.is_running = False
                task.absolute_deadline = current_time + task.deadline
        
        # Obtenir les tâches actives et calculer leur laxité
        active_tasks = []
        for task in tasks:
            if current_time >= task.arrival_time and current_time >= task.next_release and task.remaining_time > 0:
                task.laxity = task.absolute_deadline - current_time - task.remaining_time
                active_tasks.append(task)
        
        if active_tasks:
            # Trier par laxité (priorité LLF)
            active_tasks.sort(key=lambda x: x.laxity)
            highest_priority_task = active_tasks[0]
            
            # Vérifier si une interruption est nécessaire
            if current_task and current_task.id != highest_priority_task.id and current_task.remaining_time > 0:
                current_task.is_running = False
            
            current_task = highest_priority_task
            current_task.is_running = True
            
            timeline.append((current_task.id, current_time, current_time + 1))
            current_task.remaining_time -= 1
            current_task.current_execution += 1
            
            if current_task.remaining_time == 0:
                current_task.next_release = current_time + 1 - current_task.current_execution + current_task.period
                current_task.is_running = False
                current_task = None
        else:
            timeline.append(("Idle", current_time, current_time + 1))
            current_task = None
        
        current_time += 1
    
    return timeline

def fcfs_schedule(tasks, simulation_time):
    timeline = []
    current_time = 0
    tasks = deepcopy(tasks)
    ready_queue = []
    current_task = None
    
    while current_time < simulation_time:
        # Vérifier les nouvelles instances de tâches
        for task in tasks:
            if current_time >= task.arrival_time and task.remaining_time > 0:
                ready_queue.append(task)
                task.remaining_time = task.execution_time
                task.current_execution = 0
                task.is_running = False
                task.next_release += task.period  # Mettre à jour la prochaine libération
        
        if not current_task and ready_queue:
            current_task = ready_queue.pop(0)
            current_task.is_running = True
        
        if current_task:
            timeline.append((current_task.id, current_time, current_time + 1))
            current_task.remaining_time -= 1
            current_task.current_execution += 1
            
            if current_task.remaining_time == 0:
                current_task = None
        else:
            timeline.append(("Idle", current_time, current_time + 1))
        
        current_time += 1
    
    return timeline

def sjf_schedule(tasks, simulation_time):
    timeline = []
    current_time = 0
    tasks = deepcopy(tasks)
    ready_queue = []
    current_task = None
    
    while current_time < simulation_time:
        # Vérifier les nouvelles instances de tâches
        for task in tasks:
            if current_time >= task.arrival_time and task.remaining_time > 0:
                ready_queue.append(task)
                task.remaining_time = task.execution_time
                task.current_execution = 0
                task.is_running = False
                task.next_release += task.period  # Mettre à jour la prochaine libération
        
        if not current_task and ready_queue:
            # Sélectionner la tâche avec le plus petit temps d'exécution
            ready_queue.sort(key=lambda x: x.execution_time)
            current_task = ready_queue.pop(0)
            current_task.is_running = True
        
        if current_task:
            timeline.append((current_task.id, current_time, current_time + 1))
            current_task.remaining_time -= 1
            current_task.current_execution += 1
            
            if current_task.remaining_time == 0:
                current_task = None
        else:
            timeline.append(("Idle", current_time, current_time + 1))
        
        current_time += 1
    
    return timeline

def create_gantt_chart(timeline, tasks, title):
    # Créer un dictionnaire pour stocker les données de chaque tâche
    task_data = {}
    colors = {
        1: '#2ecc71',  # Vert pour T1
        2: '#3498db',  # Bleu pour T2
        3: '#34495e',  # Gris foncé pour T3
    }
    
    # Organiser les données par tâche
    for task_id, start, end in timeline:
        if task_id == "Idle":
            continue
            
        if task_id not in task_data:
            task_data[task_id] = {
                'x': [],
                'y': [],
                'color': colors.get(task_id, '#95a5a6')  # Couleur par défaut si id > 3
            }
        
        task_data[task_id]['x'].extend([start, end, None])
        task_data[task_id]['y'].extend([f"T{task_id}", f"T{task_id}", None])
    
    fig = go.Figure()
    
    # Ajouter les barres pour chaque tâche
    for task_id in sorted(task_data.keys()):  # Trier par ID de tâche
        data = task_data[task_id]
        fig.add_trace(go.Scatter(
            x=data['x'],
            y=data['y'],
            line=dict(color=data['color'], width=30),
            mode='lines',
            name=f'T{task_id}'
        ))
    
    # Configurer la mise en page
    fig.update_layout(
        title=title,
        xaxis_title="Temps",
        yaxis_title="Tâches",
        showlegend=True,
        height=300,
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGray',
            showline=True,
            linewidth=2,
            linecolor='Black',
            range=[0, max(t[2] for t in timeline)],  # Définir la plage de l'axe X
            dtick=2  # Marquer chaque unité de temps
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGray',
            showline=True,
            linewidth=2,
            linecolor='Black',
            autorange='reversed'  # Inverser l'axe Y pour avoir T1 en haut
        ),
        plot_bgcolor='white',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    # Ajouter des lignes verticales pour les périodes
    for task in tasks:
        for i in range(0, int(max(t[2] for t in timeline)), task.period):
            fig.add_shape(
                type="line",
                x0=i,
                x1=i,
                y0=f"T{task.id}",
                y1=f"T{task.id}",
                line=dict(color="black", width=1, dash="dot"),
            )
    
    return fig
