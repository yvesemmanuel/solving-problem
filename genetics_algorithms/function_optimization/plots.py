import plotly.graph_objects as go


def exp_mean_fitness_per_generation(result, title):
    x_values = list(range(len(result['mean_fitness_per_generation'])))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x_values, y=result['mean_fitness_per_generation'], mode='lines'))

    fig.update_layout(
        title=title,
        xaxis_title='Generation',
        yaxis_title='Fitness'
    )

    fig.show()


def exp_mean_n_best_fit_per_ite(result, title):
    x_values = list(range(len(result['mean_fitness_per_generation'])))

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x_values, y=result['mean_fitness_per_generation'], mode='lines', name='Mean Fitness'))
    fig.add_trace(go.Scatter(
        x=x_values, y=result['best_fitness_per_generation'], mode='lines', name='Min Fitness'))

    fig.update_layout(
        title=title,
        xaxis_title='Iteration',
        yaxis_title='Fitness'
    )

    fig.show()
