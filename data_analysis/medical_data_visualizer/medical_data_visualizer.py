import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
bmi = df["weight"] / (df["height"] / 100)**2
df['overweight'] = np.where(bmi > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df[["cholesterol", "gluc"]] = np.where(df[["cholesterol", "gluc"]] <= 1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat["total"] = 1  # necessary for catplot -> stores the value count
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    ax = sns.catplot(data=df_cat, x="variable", y="total", hue="value", kind="bar", col="cardio")

    # Get the figure for the output
    fig = ax.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df["height"] >= df["height"].quantile(0.025)) &
                 (df["height"] <= df["height"].quantile(0.975)) &
                 (df["weight"] >= df["weight"].quantile(0.025)) &
                 (df["weight"] <= df["weight"].quantile(0.975))
                ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr, mask=mask, square=True, linewidths=1., annot=True, fmt=".1f", center=0.08, cbar_kws={"shrink":.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig