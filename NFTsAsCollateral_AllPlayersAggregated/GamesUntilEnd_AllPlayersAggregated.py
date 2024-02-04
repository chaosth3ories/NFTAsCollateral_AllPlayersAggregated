import pandas as pd


# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Anzahl der Runden (Sessions) pro Spieler
sessions_per_player = data.groupby('depositor')['roundid'].nunique()

# Durchschnittliche und mediane Anzahl der Sessions pro Spieler
average_sessions_per_player = sessions_per_player.mean()
median_sessions_per_player = sessions_per_player.median()

# Ausgabe der Ergebnisse
print(f"Durchschnittliche Anzahl der Sessions pro Spieler: {average_sessions_per_player:.2f}")
print(f"Median der Anzahl der Sessions pro Spieler: {median_sessions_per_player:.2f}")

