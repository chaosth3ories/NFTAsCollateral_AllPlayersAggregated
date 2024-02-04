import pandas as pd

# Einlesen der Daten aus der CSV-Datei
data = pd.read_csv('/Users/juliuswalkenhorst/Desktop/University/9. Semester/Bachelorarbeit/Empirie/NFTsAsCollateral/DuneMaster.csv')

# Berechnung des Gesamteinsatzes pro Runde in USD
total_bets_per_round = data.groupby('roundid')['deposit_usd'].sum()

# Zuordnung des Gesamteinsatzes jeder Runde zu den individuellen Wetten
data['total_bet_round'] = data['roundid'].map(total_bets_per_round)

# Berechnung der individuellen Gewinnwahrscheinlichkeit
data['win_probability'] = data['deposit_usd'] / data['total_bet_round']

# Berechnung der durchschnittlichen und medianen Gewinnwahrscheinlichkeit
average_probability = data['win_probability'].mean()
median_probability = data['win_probability'].median()

# Ausgabe der Wahrscheinlichkeiten
print(f"Average Winning Probability: {average_probability}")
print(f"Median Winning Probability: {median_probability}")

