import matplotlib.pyplot as plt
import pandas as pd
if __name__ == "__main__":
    data_set_path = "../data_set/pokemon_alopez247.csv"
    df = pd.read_csv(data_set_path)
    df_1 = df[["Name", "Height_m", "Weight_kg", "Body_Style"]]
    ax = plt.gca()
    df_1.iloc[:30].plot(kind="line", x="Name", y="Height_m", ax=ax)
    df_1.iloc[:30].plot(kind="line", x="Name", y="Weight_kg", ax=ax, color="red")
    plt.show()