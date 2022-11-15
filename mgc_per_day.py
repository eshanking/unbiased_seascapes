import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from fears.utils import plotter
from cycler import cycler 

fig,ax = plt.subplots()

df = pd.read_excel('max_conc_per_day.xlsx')
df = df.melt(id_vars='Replicate',var_name='Day',value_name='MGC (ug/mL)')

ax = sns.stripplot(data=df,y='MGC (ug/mL)',x='Day',hue='Replicate',
                    ax=ax,size=7,jitter=1)
ax.set(yscale="log")

ax.get_legend().remove()

fig2,ax2 = plt.subplots(figsize=(5,4))
# cc = plotter.gen_color_cycler()

# ax2.set_prop_cycle(cc)
cm = mpl.cm.get_cmap('magma')

df = pd.read_excel('max_conc_per_day.xlsx')

for row in range(df.shape[0]):
    y = df.loc[row]
    y = y[1:]
    ax2.plot(y,label=str(row),color=cm(row/12))

ax2.set_yscale('log')
ax2.set_ylabel('MGC (ug/mL)',fontsize=14)
ax2.set_xlabel('Days',fontsize=14)

fig2.legend(loc=(0.64,0.17),frameon=False,ncol=2,title='replicate',title_fontsize=12)

ax2.tick_params(axis='both', labelsize=12)

fig2.savefig('MGC_per_day.pdf',bbox_inches='tight')