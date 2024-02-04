import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Filtern der Daten auf Einträge mit einem ENS-Namen
players_with_ens = data[~data['ens_name'].isna() & (data['ens_name'] != '')]

# Zählen der einzigartigen Spieler mit einem ENS-Namen
unique_players_with_ens = players_with_ens['depositor'].nunique()

# Ausgabe der Anzahl
print(f"Amount of Players with an ENS-Name: {unique_players_with_ens}")
