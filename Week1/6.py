import pandas as pd


data = {
    "Noise": ["Jackhammer", "Gas lawnmower", "Alarm clock", "Quiet room"],
    "Decibel level (dB)": [130, 106, 70, 40]
}

df = pd.DataFrame(data)
df = df.sort_values(by="Decibel level (dB)").reset_index(drop=True)


def determine_noise_level(db_level):
    if db_level < df["Decibel level (dB)"].min():
        return "The entered decibel level is lower than the quietest noise in the table."
    elif db_level > df["Decibel level (dB)"].max():
        return "The entered decibel level is higher than the loudest noise in the table."
    else:
        for i in range(len(df)):
            if db_level == df.loc[i, "Decibel level (dB)"]:
                return f"The entered decibel level corresponds to: {df.loc[i, 'Noise']}."
            elif db_level < df.loc[i, "Decibel level (dB)"]:
                return (f"The entered decibel level is between {df.loc[i-1, 'Noise']} "
                        f"({df.loc[i-1, 'Decibel level (dB)']} dB) and {df.loc[i, 'Noise']} "
                        f"({df.loc[i, 'Decibel level (dB)']} dB).")


db_level = int(input("Enter the decibel level: "))


result = determine_noise_level(db_level)
print(result)
