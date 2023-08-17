import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = range(df["Year"].min(), 2051, 1)
    ax.plot(x, result.intercept + result.slope*x,
            color='tab:red', label="fitted line")

    # Create second line of best fit
    new_result = linregress(df["Year"][df["Year"] >= 2000],
                            df["CSIRO Adjusted Sea Level"][df["Year"] >= 2000])
    x_new = range(2000, 2051, 1)
    ax.plot(x_new, new_result.intercept + new_result.slope*x_new,
            color='orangered', label="new fitted line")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()