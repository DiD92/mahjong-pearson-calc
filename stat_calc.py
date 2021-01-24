import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

used_columns = ['First', 'Second', 'Third', 'Fourth', 'Negative', 'Win Rate', 'Tsumo Rate', 'Deal-In Rate', 'Call Rate', 'Riichi Rate', 'R. Ron', 'R. Tsumo', 'D. Ron', 'D. Tsumo']
wanted_indexes = ['Tsumo Rate', 'Deal-In Rate', 'Call Rate', 'Riichi Rate', 'R. Ron', 'R. Tsumo', 'D. Ron', 'D. Tsumo']
wanted_columns = ['First', 'Second', 'Third', 'Fourth', 'Negative', 'Win Rate']

font_common_properties = {
    'family': 'serif',
}

def extract_data_from_file(file_path):
    df = pd.read_csv(file_path)
    df = df[used_columns]
    df = df.corr(method='pearson')
    df = df.loc[wanted_indexes, wanted_columns]

    return df

def draw_plot_for_data(df):
    fig = plt.figure(figsize=(9.6, 9.6), dpi=96)
    ax = fig.add_subplot(111)
    cax = ax.matshow(df, interpolation='nearest', cmap='RdYlGn')
    fig.colorbar(cax)

    ax.set_xticklabels([''] + wanted_columns, **font_common_properties)
    ax.set_yticklabels([''] + wanted_indexes, **font_common_properties)

    for _, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(df.shape[1] + 1) -.5, minor=True)
    ax.set_yticks(np.arange(df.shape[0] + 1) -.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='solid', linewidth=0.5)
    ax.tick_params(which="minor", left=False)

    for i in range(len(wanted_indexes)):
        for j in range(len(wanted_columns)):
            data_value = df.iloc[i, j]
            color = "white" if abs(data_value) > 0.6 else "black"

            ax.text(j, i, f'{data_value:.3f}', 
                ha="center", va="center", color=color, weight='demi', size='large', 
                **font_common_properties)

    plt.savefig('plot.png')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing fiile parameter")
        exit(-1)

    fpath = sys.argv[1]

    df = extract_data_from_file(fpath)

    draw_plot_for_data(df)
