import plotly.graph_objects as go
def update_time(x):
    x = str(x)
    return x[:2] + ':' + x[2:4] + ':' + x[4:]

a = 0.3
b = 0.6
day = 20210108
df = data2021[data2021['<DATE>'] == day]
time = [update_time(x) for x in df['<TIME>']]
up2 = [list(df['<OPEN>'])[0] * (1 + a / 100)] * len(df) 
up3 = [list(df['<OPEN>'])[0] * (1 + b / 100)] * len(df) 
down2 = [list(df['<OPEN>'])[0] * (1 - b / 100)] * len(df) 
down3 = [list(df['<OPEN>'])[0] * (1 - a / 100)] * len(df) 


fig = go.Figure()

fig.add_trace(go.Scatter(x = time, y = list(df['<OPEN>']), name = '',
                         line = dict(color ='royalblue', width = 2)))

fig.add_trace(go.Scatter(x = time, y = up2, name = '',
                         line = dict(color = 'firebrick', width = 2, dash='dash')))
fig.add_trace(go.Scatter(x = time, y = down2, name = '',
                         line = dict(color = 'firebrick', width = 2, dash='dash')))
fig.add_trace(go.Scatter(x = time, y = up3, name = '',
                         line = dict(color = 'rgb(33, 183, 98)', width = 2, dash='dash')))
fig.add_trace(go.Scatter(x = time, y = down3, name = '',
                         line = dict(color = 'rgb(33, 183, 98)', width = 2, dash='dash')))
                         
fig.show()