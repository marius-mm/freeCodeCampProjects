#%%
import mchmm as mc

#%%
chain = mc.MarkovChain().from_data('RSPPSRRRSSSSPRSSPRSSRPRPPSR')
# %%
chain.observed_matrix
# %%
graph = chain.graph_make(
      format="png",
      graph_attr=[("rankdir", "LR")],
      node_attr=[("fontname", "Roboto bold"), ("fontsize", "20")],
      edge_attr=[("fontname", "Iosevka"), ("fontsize", "12")]
    )
graph.render()
# %%

# %%
