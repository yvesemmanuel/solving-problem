import plotly.graph_objects as go
import plotly.express as px

import random
import math
import statistics


def exp_mean_fitness_per_ite(result):
    exp_id = random.choice(range(len(result)))

    x_values = list(range(len(result['exps_mean_fit_per_ite'][exp_id])))

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_values, y=result['exps_mean_fit_per_ite'][exp_id], mode='lines', name='Before'))

    fig.update_layout(
        title=f'Mean Fitness per Iteration (Experiment {exp_id})',
        xaxis_title='Iteration',
        yaxis_title='Fitness'
    )

    fig.show()


def exp_mean_n_best_fit_per_ite(result):
    exp_id = random.choice(range(len(result)))

    x_values = list(range(len(result['exps_mean_fit_per_ite'][exp_id])))

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_values, y=result['exps_mean_fit_per_ite'][exp_id], mode='lines', name='Mean Fitness'))
    fig.add_trace(go.Scatter(x=x_values, y=result['exps_best_fit_per_ite'][exp_id], mode='lines', name='Max Fitness'))

    fig.update_layout(
        title=f'Mean and Max Fitness per Iteration (Experiment {exp_id})',
        xaxis_title='Iteration',
        yaxis_title='Fitness'
    )

    fig.show()


def mean_fitness_per_exp(result):

    x_values = list(range(len(result['exps_initial_mean_fit'])))

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=x_values, y=result['exps_initial_mean_fit'], mode='lines', name='Before'))

    fig.add_trace(go.Scatter(x=x_values, y=result['exps_final_mean_fit'], mode='lines', name='After', line=dict(color='red')))

    fig.update_layout(
        title='Mean fitness per Experiment',
        xaxis_title='Experiment',
        yaxis_title='Mean fitness'
    )

    fig.show()


def iterations_per_experiment(result):
    fig = px.histogram(x=result['exps_num_ite'], nbins=20)

    mean_value = sum(result['exps_num_ite']) / len(result['exps_num_ite'])

    fig.update_layout(
        title='Iterations per Experiment',
        xaxis_title='Iterations',
        yaxis_title='Experiments'
    )

    fig.add_shape(
        type="line",
        x0=mean_value,
        x1=mean_value,
        y0=0,
        y1=len(result),
        line=dict(
            color="red",
            width=2,
            dash="dash",
        )
    )

    fig.show()

def solution_found_on_per_experiment(result):
    fig = px.histogram(x=result['exps_solution_found_on'], nbins=20)

    fig.update_layout(
        title='Iterations per Experiment',
        xaxis_title='Iterations',
        yaxis_title='Experiments'
    )

    fig.show()

def plot_class_evaluations(result):
    num_experiments = len(result['exps_best_fit_per_ite'])

    best_fit_per_exp = []
    total_convergence_per_exp = []

    for exp in result['exps_best_fit_per_ite']:
        best_fit_per_exp.append(max(exp))
        total_convergence_per_exp.append(exp.count(1))

    num_convergence_exp = sum(map(math.floor, best_fit_per_exp))

    convergence_rate = num_convergence_exp / num_experiments
    total_convergence_per_exp = statistics.mean(total_convergence_per_exp)

    print(f'Convergence Rate: {convergence_rate}\nMean of total convergence: {total_convergence_per_exp}')

    mean_num_ite = statistics.mean(result['exps_num_ite'])
    std_num_ite = statistics.stdev(result['exps_num_ite'])

    print(f'Mean Num. Iterations: {mean_num_ite}\nStd. Num. Iterations: {std_num_ite}')

    mean_population_fit_per_exp = statistics.mean(result['exps_final_mean_fit'])
    std_population_fit_per_exp = statistics.stdev(result['exps_final_mean_fit'])

    print(f'Mean Pop. Fitness: {mean_population_fit_per_exp}\nStd. Pop. Fitness: {std_population_fit_per_exp}')
