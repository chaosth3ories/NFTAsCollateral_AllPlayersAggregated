import pandas as pd


# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Berechnen des Gesamteinsatzes der Verlierer pro Runde
loser_bet_per_round = data[data['is_winner'] == 0].groupby('roundid')['deposit_usd'].sum()

# Verlust pro Runde (Gesamteinsatz der Verlierer)
loss_per_round = loser_bet_per_round

# Durchschnittlicher und medianer Verlust pro Runde
average_loss = loss_per_round.mean()
median_loss = loss_per_round.median()

# Höchster und niedrigster Verlust in einer Runde
max_loss = loss_per_round.max()
min_loss = loss_per_round.min()

# Ausgabe der Ergebnisse
print(f"Durchschnittlicher Verlust pro Runde: {average_loss}")
print(f"Medianer Verlust pro Runde: {median_loss}")
print(f"Höchster Verlust in einer Runde: {max_loss}")
print(f"Niedrigster Verlust in einer Runde: {min_loss}")
