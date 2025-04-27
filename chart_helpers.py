import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.dpi"] = 300
plt.rcParams["boxplot.medianprops.color"] = "black"


colors = {
    "Snatch FirstAttempt": "#AEE2FF",
    "Snatch SecondAttempt": "#93C6E7",
    "Snatch ThirdAttempt": "#578FCA",
    "Clean And Jerk FirstAttempt": "#F0F1C5",
    "Clean And Jerk SecondAttempt": "#BBD8A3",
    "Clean And Jerk ThirdAttempt": "#6F826A",
    "Snatch Result": "#8967B3",
    "Clean And Jerk Result": "#8967B3",
    "Snatch": "#93C6E7",
    "CleanAndJerk": "#BBD8A3",
    "Total": "#8967B3"
}

map_vars_to_ptbr = {
    "FirstAttempt": "1ª Tentativa",
    "SecondAttempt": "2ª Tentativa",
    "ThirdAttempt": "3ª Tentativa",
    "Result": "Resultado",
}

def plot_top5_attempts(top5: pd.DataFrame, exercise = "", category="96kg"):
    metrics = ["FirstAttempt", "SecondAttempt", "ThirdAttempt", "Result"]
    athletes = top5['Name']
    bar_height = 0.2
    x = np.arange(len(athletes))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    for i, metric in enumerate(metrics):
        bars = ax.barh(x + i * bar_height, top5[metric], height=bar_height, label=map_vars_to_ptbr[metric], color=colors[f"{exercise} {metric}"])

        for bar in bars:
            width = bar.get_width()
            y = bar.get_y() + bar.get_height() / 2
            ax.text(
                width + 0.1, 
                y, 
                f'{width:.0f}{"kg" if metric in ["Result", "Total"] else ""}', 
                va='center', 
                fontsize=(9 if metric in ["Result", "Total"] else 6), 
                color=("black" if metric in ["Result", "Total"] else "gray")
            )

    ax.set_yticks(x + bar_height * (len(metrics)-1) / 2)
    ax.set_yticklabels(athletes)

    plt.title(
        f"Uma tentativa a um peso pode não ter sucesso. O Resultado é o levantamento de sucesso mais pesado por um atleta",
        fontsize=8,
        pad=10,
        loc="left",
        color="grey"
    )

    plt.suptitle(
        f"Top 5 atletas por resultado em {exercise if len(exercise) > 0 else 'NULL'} na categoria {category}",
        fontsize=12,
        fontweight="bold",
        x=0.175,
        y=0.96,
        ha="left",
    )

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.invert_yaxis() # fix problem in which the order of athletes is reversed
    plt.tight_layout()
    plt.show()


def plot_total_info(total: pd.DataFrame, xy, category="96kg"):
    metrics = ["Snatch", "CleanAndJerk", "Total"]
    athletes = total['Name']
    bar_height = 0.2
    x = np.arange(len(athletes))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    for i, metric in enumerate(metrics):
        bars = ax.barh(x + i * bar_height, total[metric], height=bar_height, label=(metric if metric != "CleanAndJerk" else "Clean and Jerk"), color=colors[metric])
        for bar in bars:
            width = bar.get_width()
            y = bar.get_y() + bar.get_height() / 2
            ax.text(
                width + 0.1, 
                y, 
                f'{width:.0f}{"kg" if metric in ["Result", "Total"] else ""}', 
                va='center', 
                fontsize=(9 if metric in ["Result", "Total"] else 6), 
                color=("black" if metric in ["Result", "Total"] else "gray")
            )

    ax.set_yticks(x + bar_height * (len(metrics)-1) / 2)
    ax.set_yticklabels(athletes)

    # ax.set_title(f"Athlete Totals")

    plt.title(
        f"O Total é a soma do melhor resultado em Snatch e Clean and Jerk",
        fontsize=8,
        pad=10,
        loc="left",
        color="grey"
    )

    plt.suptitle(
        f"Top 5 atletas por Total em {category}",
        fontsize=12,
        fontweight="bold",
        x=xy[0],
        y=xy[1],
        ha="left",
    )

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.invert_yaxis() # fix problem in which the order of athletes is reversed
    plt.tight_layout()
    plt.show()

def histogram(data: pd.Series, title="Title", vline_value = -1):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    bins = len(data)//2 if len(data) > 100 else len(data)
    ax.hist(data, bins=bins)

    data_min = np.min(data)
    data_max = np.max(data)
    is_integer = np.issubdtype(data.dtype, np.integer)
    
    xticks = np.linspace(data_min, data_max, num=6)
    if is_integer:
        labels = [f'{int(x)}' for x in xticks]
    else:
        labels = [f'{x:.1f}' for x in xticks]
    plt.xticks(xticks, labels)

    if vline_value > -1:
        ax.axvline(
            vline_value,
            linestyle='--', 
            alpha=0.7,
            color="grey",
            label="Karlos Nasar"
        )
        plt.legend()

    plt.title(
        title,
        fontsize=12,
        fontweight="bold",
        pad=10,
        loc="left"
    )
    plt.show()