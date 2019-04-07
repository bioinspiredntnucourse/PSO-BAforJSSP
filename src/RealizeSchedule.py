import matplotlib.pyplot as plt
import pandas as pd
import random
import io

inp = u"""a0:86:c6:52:4e:e8,0.006568,0.006620,Out
a0:86:c6:52:4e:e8,0.006663,0.006695,In
a0:86:c6:52:4e:e8,0.008089,0.008141,Out
a0:86:c6:52:4e:e8,0.008185,0.008217,In
01:00:5e:00:00:fb,0.033096,0.035016,Out
33:33:00:00:00:fb,0.034997,0.037077,Out
01:00:5e:7f:ff:fa,0.039969,0.042057,Out
ff:ff:ff:ff:ff:ff,0.059823,0.061639,Out
a0:86:c6:52:4e:e8,0.068865,0.068917,Out
a0:86:c6:52:4e:e8,0.068962,0.068994,In
a0:86:c6:52:4e:e8,0.083492,0.083544,Out
a0:86:c6:52:4e:e8,0.083588,0.083620,In"""

def save_schedule(solution):
    print("save_schedule() function not implemented")
    return None

def plot_schedule(num_jobs):
    df = pd.read_csv(io.StringIO(inp), header=None, names=["Resource", "Start", "Finish", "Operation"] )
    df["Diff"] = df.Finish - df.Start

    operation_color = []
    for i in range(num_jobs):
        operation_color = random.randint(0,4)

    fig,ax=plt.subplots(figsize=(6,3))

    labels=[]
    for i, resource in enumerate(df.groupby("Resource")):
        labels.append(resource[0])
        for r in resource[1].groupby("Operation"):
            data = r[1][["Start", "Diff"]]
            ax.broken_barh(data.values, (i-0.4,0.8), color='b' )

    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xlabel("time")
    plt.tight_layout()
    plt.show()
