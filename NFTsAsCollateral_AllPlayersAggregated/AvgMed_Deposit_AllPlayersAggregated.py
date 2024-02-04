import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnung des durchschnittlichen und medianen Einsatzes aller Spieler
average_bet_all_players = data['deposit_usd'].mean()
median_bet_all_players = data['deposit_usd'].median()

# Ausgabe der durchschnittlichen und medianen Einsatzhöhe aller Spieler
print(f"Durchschnittlicher Einsatz aller Spieler: {average_bet_all_players}")
print(f"Median des Einsatzes aller Spieler: {median_bet_all_players}")
