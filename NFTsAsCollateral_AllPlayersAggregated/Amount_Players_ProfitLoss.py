import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Identifizieren der Gewinne und Verluste (Annahme: Einsatz für Verlierer als Verlust, für Gewinner als Gewinn)
data['result'] = data.apply(lambda row: row['deposit_usd'] if row['is_winner'] == 1 else -row['deposit_usd'], axis=1)

# Berechnen des Gesamtgewinns/-verlustes pro Spieler
total_result_per_player = data.groupby('depositor')['result'].sum()

# Identifizieren, ob ein Spieler im Profit oder Verlust ist
players_in_profit = total_result_per_player[total_result_per_player > 0].count()
players_in_loss = total_result_per_player[total_result_per_player < 0].count()

# Ausgabe der Ergebnisse
print(f"Anzahl der Spieler im Profit: {players_in_profit}")
print(f"Anzahl der Spieler im Verlust: {players_in_loss}")
