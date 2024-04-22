import pandas as pd
import plotly.graph_objects as go
import os
import glob

csv_files = glob.glob('stored_results/results_*.csv')
csv_latest = max(csv_files, key=os.path.getmtime)
server_files = glob.glob('stored_results/server_*.txt')
server_latest = max(server_files, key=os.path.getmtime)
print("Latest", server_files, server_latest)

df = pd.read_csv(csv_latest)

# fig = px.line(df, x='time', y=['curr_ping', 'curr_upload', 'curr_download', 'avg_ping', 'avg_upload_speed',
#                                'avg_download_speed'], title='Speedtest Stats', markers=True)
fig = go.Figure()
fig.add_scatter(x=df['time'], y=df['curr_ping'], name='Ping(ms)')
fig.add_scatter(x=df['time'], y=df['curr_upload'], name='Upload(Mbps)')
fig.add_scatter(x=df['time'], y=df['curr_download'], name='Download(Mbps)')
fig.add_scatter(x=df['time'], y=df['avg_ping'], name='Avg Ping(ms)')
fig.add_scatter(x=df['time'], y=df['avg_upload_speed'] / 1000000, name='Avg Upload(Mbps)')
fig.add_scatter(x=df['time'], y=df['avg_download_speed'] / 1000000, name='Avg Download(Mbps)')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1y <", step="year", stepmode="backward"),
            dict(count=6, label="6m <", step="month", stepmode="backward"),
            dict(count=1, label="1m <", step="month", stepmode="backward"),
            dict(count=1, label="Now", step="day", stepmode="todate"),
            dict(count=1, label="Now Month", step="month", stepmode="todate"),
            dict(count=1, label="Now Year", step="year", stepmode="todate"),
            dict(step="all")
        ])
    )
)
with open(server_latest, 'r') as file:
    serverDetails = file.read().replace('\n', '')

fig.update_layout(title='Speedtest Statistics - ' + serverDetails, xaxis_title='Date', yaxis_title='Measure Value', plot_bgcolor='silver',
                  legend=dict(title='Measure', bgcolor='silver', font_color='black'), font_color='black')
fig.update_traces(marker_symbol='x')
fig.show()
