import math

import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

def series_gcd(start, end_exclusive):
    gcd = np.longlong(0)
    for number in range(start, end_exclusive):
        gcd = np.longlong(np.gcd(gcd, number))
    if gcd == 0:
        return np.nan
    return gcd


def series_lcm(start, end_exclusive):
    # gcd = series_gcd(start, end_exclusive)
    # if gcd == math.nan:
    #     return math.nan
    # return np.prod(range(start, end_exclusive))/gcd
    lcm = np.longlong(1)
    for number in range(start, end_exclusive):
        lcm = np.longlong(np.lcm(lcm, number))
    if lcm == 1:
        return np.nan
    return lcm


def generate_lcm_gcd(size_x: int, size_y: int):
    return np.array([[[series_gcd(x, y), series_lcm(x, y)] for x in range(1, size_x)] for y in range(1, size_y)])


max_start = 42
max_end = 42
lcm_gcd = generate_lcm_gcd(max_start, max_end)
# lcm_gcd=np.log2(lcm_gcd)
x = tuple(range(1, max_start))
y = tuple(range(1, max_end))
gcd = go.Surface(z=lcm_gcd[:, :, 0], x=x, y=y, )
lcm = go.Surface(z=lcm_gcd[:, :, 1], x=x, y=y, )
gcd_data = lcm_gcd[:, :, 0]
lcm_data = lcm_gcd[:, :, 1]
gcd_data_log2 = np.log2(lcm_gcd[:, :, 0])
lcm_data_log2 = np.log2(lcm_gcd[:, :, 1])
data = [gcd]

# fig = make_subplots(rows=2, cols=2,
#                     specs=[[{'type': 'surface'}, {'type': 'surface'}],
#                            [{'type': 'surface'}, {'type': 'surface'}]])
# fig.add_trace(gcd, row=1, col=1)
# fig.add_trace(lcm, row=1, col=2)

fig = go.Figure(data=data)

#
# [ {'x':[filtered['date']], 'y':[filtered[metric]], 'name':filter_name},
#   {'title':filter_name} ]

A = 0
B = 0
C = 0


def set_state(a, b, c):
    A, B, C =1, 1, 1

fig.update_layout(
    title="GCD for series from x to y (exclusive)",
    xaxis_title="From number",
    yaxis_title="To number (exclusive)",
    updatemenus=[
        dict(
            buttons=[
                dict(
                    args=[
                        {"z": [gcd_data]},
                        {"title": "GCD for series from x to y (exclusive)"}],
                    label="GCD",
                    method="update",
                ),
                dict(
                    args=[{"z": [lcm_data]},
                          {"title": "LCM for series from x to y (exclusive)"}],
                    label="LCM",
                    method="update"
                ),
                dict(
                    args=[{"z": [gcd_data_log2]},
                          {"title": "Logarithmized(log2) GDC for series from x to y (exclusive)"}],
                    label="log2(GCD)",
                    method="update"
                ),
                dict(
                    args=[{"z": [lcm_data_log2]},
                          {"title": "Logarithmized(log2) LCM for series from x to y (exclusive)"}],
                    label="log2(LCM)",
                    method="update"
                )
            ],
            active=0,
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
        dict(
            buttons=[
                dict(
                    args=[{"type": "surface"}],
                    label="Surface",
                    method="restyle"
                ),
                dict(
                    args=[{"type": "heatmap"}],
                    label="Heatmap",
                    method="restyle"
                )
            ],
            active=0,
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.3,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)
# fig.show()

print(F"{A}, {B}, {C}")