import pandas as pd

# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Identifizieren aller einzigartigen Spieler und Zählen ihrer gespielten Runden
rounds_per_player = data.groupby('depositor')['roundid'].nunique()

# Ermitteln der Anzahl der Spieler, die nur eine Runde gespielt haben
one_round_players = rounds_per_player[rounds_per_player == 1].count()

# Gesamtzahl der einzigartigen Spieler
total_unique_players = rounds_per_player.count()

# Berechnen der Churn Rate
churn_rate = (one_round_players / total_unique_players) * 100

# Ausgabe der Churn Rate
print(f"Churn Rate: {churn_rate:.2f}%")
