import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# 1. Gesamtanzahl aller Spiele (Runden)
total_games = data['roundid'].nunique()

# 2. Gesamtanzahl der einzelnen Spieler
total_players = data['depositor'].nunique()

# 3. Anzahl der abgebrochenen Runden
aborted_rounds = data['is_too_little_players'].sum()

# 4. Anzahl der unclaimed Gewinne
unclaimed_wins = data['is_unclaimed'].sum()

# 5. Gesamtvolumen in ETH und USD
total_volume_eth = data['deposit_eth'].sum()
total_volume_usd = data['deposit_usd'].sum()

# Ausgabe der Ergebnisse
print(f"Gesamtanzahl aller Spiele (Runden): {total_games}")
print(f"Gesamtanzahl der einzelnen Spieler: {total_players}")
print(f"Anzahl der abgebrochenen Runden: {aborted_rounds}")
print(f"Anzahl der unclaimed Gewinne: {unclaimed_wins}")
print(f"Gesamtvolumen in ETH: {total_volume_eth}")
print(f"Gesamtvolumen in USD: {total_volume_usd}")
