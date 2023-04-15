import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

csv = pd.read_csv("video_games_sales.csv")

fig_na = px.treemap(csv,
                 path=[px.Constant("World Sales Flatform"), "platform", "genre"],
                 values='global_sales',
                 color='na_sales',
                 color_continuous_scale='viridis'
                 )

fig_jp = px.treemap(csv,
                 path=[px.Constant("World Sales Flatform"), "platform", "genre"],
                 values='global_sales',
                 color='jp_sales',
                 color_continuous_scale='viridis'
                 )

fig_eu = px.treemap(csv,
                 path=[px.Constant("World Sales Flatform"), "platform", "genre"],
                 values='global_sales',
                 color='eu_sales',
                 color_continuous_scale='viridis'
                 )


print(fig_na.show())
print("\n")
print(fig_jp.show())
print("\n")
print(fig_eu.show())
    