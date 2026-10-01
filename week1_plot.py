import pandas as pd
import matplotlib.pyplot as plt
df_teeth = pd.read_csv("mammal_teeth.csv")


plt.figure(figsize=(5, 10)) 
plt.scatter(x=df_teeth['Top incisors'],
            y=df_teeth['MAMMAL'])

plt.gca().xaxis.set_visible(False)

plt.title(" Tamara's plot for mammal_teeth dataset")
plt.savefig("mammal_teeth_scatterplot.png", dpi=150) 
