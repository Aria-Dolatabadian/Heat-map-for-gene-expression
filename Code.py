import pandas as pd
df = pd.read_csv (r'Heat.csv')
print (df)
# set gene names as index
df = df.set_index(df.columns[0])
from bioinfokit import analys, visuz
# heatmap with hierarchical clustering
visuz.gene_exp.hmap(df=df, cmap='RdYlGn', dim=(3, 6), tickfont=(6, 4), show=True)
# heatmap without hierarchical clustering
# visuz.gene_exp.hmap(df=df, cmap='RdYlGn', colclus=False, rowclus=False, dim=(3, 6), tickfont=(6, 4), show=True)
