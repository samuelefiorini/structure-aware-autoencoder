import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from wordcloud import WordCloud

from ..utils import flatten


def radar(df, idx):
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values = df.loc[idx].values.flatten().tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(df.shape[1]) * 2 * np.pi for n in range(df.shape[1])]
    angles += angles[:1]

    fig = plt.figure(figsize=(6, 6))
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], df.columns, color='k', size=15)
    plt.yticks([0, .25, .5, .75, 1], ["0%", '25%', "50%", '75%', "100%"],
               color="grey",
               size=15)
    plt.ylim([0, 1])

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)


def lollipop_h(df, idx):
    values = df.loc[idx].values.flatten().tolist()
    fig = plt.figure(dpi=100)
    colors = [i for i in sns.color_palette('deep')]
    plt.hlines(y=df.columns, xmin=0, xmax=values, colors=colors, linewidth=4)
    for i, x, c in zip(range(len(values)), values, colors):
        plt.plot(x, i, 'o', color=c, markersize=10)
    plt.xlim([0, 1])
    sns.despine(left=False, bottom=True)
    return plt


def lollipop_v(df, idx):
    values = df.loc[idx].values.flatten().tolist()
    fig = plt.figure(dpi=100)
    colors = [i for i in sns.color_palette('deep')]
    plt.vlines(x=df.columns, ymin=0, ymax=values, colors=colors, linewidth=4)
    for i, x, c in zip(range(len(values)), values, colors):
        plt.plot(i, x, 'o', color=c, markersize=10)
    plt.ylim([0, 1])
    plt.xticks(rotation=45)
    sns.despine(left=True, bottom=False)
    return plt


def lollipop(df, idx, orientation='vertical'):
    if orientation.lower() == 'vertical':
        return lollipop_v(df, idx)
    elif orientation.lower() == 'horizontal':
        return lollipop_h(df, idx)
    else:
        print('Orientation {} not understood'.format(orientation))


def wordcloud(df, idx):
    x, y = np.ogrid[:300, :300]
    mask = (x - 150)**2 + (y - 150)**2 > 130**2
    mask = 255 * mask.astype(int)

    values = df.loc[idx].values.flatten().tolist()
    text = []
    for c, v in zip(df.columns, values):
        text.append([c.replace(' ', '_')] * int(10 * v))
    text = flatten(text)
    text = ' '.join(text)

    wc = WordCloud(
        mask=mask,
        background_color='white',
        colormap='Paired',
        max_font_size=100,
        min_font_size=1,
        contour_width=1,
        contour_color='gray').generate(text)
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    return plt
