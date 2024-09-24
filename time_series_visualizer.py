import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

# Filter out the outliers
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]


def draw_line_plot():
    # Draw line plot
    df['date'] = pd.to_datetime(df['date'])

    # Plot the data
    fig = plt.plot(df['date'], df['value'], 'r', linewidth=1)

    # Title and labels
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.strftime('%B')
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind='bar', ax=ax)
    ax.legend(title='Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, order=months_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
