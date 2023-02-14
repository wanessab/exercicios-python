"""import matplotlib.pyplot as plt

produtos = ["Produto a", "Produto B", "Produto C", "Produto D", "Produto E"]
qdt_estoque = [500,200,400,200,50]

plt.plot(produtos,qdt_estoque)
plt.show()
"""
"""""""""
import plotly.express as px
import pandas as pd

dados_x=["2018","2019","2020","2021","2022"]
dados_y=[100,200,150,90,120]

fig = px.line(x = dados_x, y = dados_y, title= "Professores x Ano", height= 400, width= 1000, line_shape = "spline")
fig.show()


import plotly.express as px
import pandas as pd

dados_x=["2018","2019","2020","2021","2022"]
dados_y=[100,200,150,90,120]

fig = px.line(x = dados_x, y = dados_y, title= "Professores x Ano", height= 400, width= 1000,)
fig.update_yaxes(title = "Professores",title_font_color = "red", ticks ="outside", tickfont_color="blue")
fig.show()
"""



