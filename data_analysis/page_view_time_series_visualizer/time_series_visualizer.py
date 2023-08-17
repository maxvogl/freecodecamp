import locale
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) &
        (df["value"] <= df["value"].quantile(0.975))
       ]

def draw_line_plot():
    # Draw line plot
    fig, ax=plt.subplots(figsize=(32, 10), dpi=100)
    df.plot(color="r", linewidth=2, ax=ax, legend=False)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    missing_months = pd.DataFrame({"Years": [2016]*4,
                                   "Months": ["January", "February", "March", "April"],
                                   "value": [0]*4})
    df_bar = pd.concat([missing_months, df_bar])
    df_pivot = pd.pivot_table(data=df_bar,
                              values="value",
                              index="Years",
                              columns="Months",
                              aggfunc="mean",
                              sort=False
                             )

    # Draw bar plot
    fig, ax=plt.subplots(figsize=(15.14,13.30), dpi=100)
    df_pivot.plot.bar(ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ['Jan', 'Feb', 'Mar',
              'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig, ax=plt.subplots(nrows=1, ncols=2, figsize=(28.8, 10.8), dpi=100)
    sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    # ax[0].set_ylim(0, 200000)

    sns.boxplot(data=df_box, x="month", y="value", order=months, ax=ax[1])
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    # ax[1].set_ylim(0, 200000)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
