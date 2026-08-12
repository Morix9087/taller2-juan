# %% [markdown]
# # Punto 2

# %% [markdown]
# ### Operación 1:
# Cargue de datos.

# %%
import pandas as pd
df = pd.read_csv("BikePrices.csv")
df

# %% [markdown]
# ### Operación 2:
# Se realiza una revisión de los datos faltantes.

# %%
df.isna().sum()

# %% [markdown]
# ### Operación 3:
# Se eliminan los datos sin variable "Ex_Showroom_Price", con el fin de que no afecten los resultados. Esto se hace ya que interpolar o completar una cantidad tan grande de datos puede causar errores en la medición y con su eliminación se sigue contando con una gran muestra de datos.

# %%
df = df.iloc[:626]
df

# %% [markdown]
# ### Operación 4:
# Se estudia la correlación entre los datos numéricos.

# %%
df2 = df.copy()
del df2['Brand']
del df2['Model']
del df2['Seller_Type']
del df2['Owner']

df2.corr()


# %% [markdown]
# ### Operación 5:
# Se estudia la covarianza entre los datos numéricos.

# %%
df2.cov()

# %% [markdown]
# ### Operación 6:
# La variable numerica "Year" se convierte en categorica bajo los nombres: Muy antigua, Antigua, Nueva, Muy nueva 

# %%
año = df['Year']
bins = [2000, 2011, 2014, 2017, 2020]
nombres_cats = ['Muy antigua', 'Antigua', 'Nueva', 'Muy nueva']
años_cat = pd.cut(año, bins, labels=nombres_cats)
años_cat

# %% [markdown]
# ### Operación 7:
# Se cuentan las bicicletas por categoria de antigüedad.

# %%
años_cat.value_counts()

# %% [markdown]
# ### Operación 8:
# Se agregan variables dummies para expresar binariamente los años de cada bicicleta

# %%
años_cat_dummies = pd.get_dummies(años_cat, dtype=int)
años_cat_dummies

# %% [markdown]
# ### Operación 9:
# Eliminar temporalmente las columnas diferentes a los precios

# %%
df_temp = df.drop(columns=["Brand","Model","Year","Seller_Type","Owner","KM_Driven"])
df_temp

# %% [markdown]
# ### Operación 10:
# Añadir nueva columna correspondiente a la diferencia del precio de compra y precio de venta

# %%
df_temp["Difference"]=df_temp["Ex_Showroom_Price"]-df_temp["Selling_Price"]
df_temp


