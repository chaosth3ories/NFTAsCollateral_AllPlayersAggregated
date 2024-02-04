import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


# Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Konvertierung der 'block_time' in datetime-Objekte und Extraktion der Stunden
data['block_time'] = pd.to_datetime(data['block_time'])
data['hour'] = data['block_time'].dt.hour + data['block_time'].dt.minute / 60

# Erstellen eines Histogramms für die Spielzeiten
fig, ax1 = plt.subplots(figsize=(10, 6))

# Histogramm für die Spielzeiten
ax1.hist(data['hour'], bins=np.arange(0, 24, 1), alpha=0.75, color='blue', label='Amount of Games')
ax1.set_xlabel('Time (Hours)')
ax1.set_ylabel('Amount of Games', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Zweite Y-Achse für die durchschnittliche Einsatzhöhe
ax2 = ax1.twinx()
average_deposit_per_hour = data.groupby(data['block_time'].dt.hour)['deposit_eth'].mean()
ax2.plot(average_deposit_per_hour.index, average_deposit_per_hour, color='red', label='Average Deposit (ETH)', marker='o')
ax2.set_ylabel('Average Deposit (ETH)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Titel und Legende
plt.title('Betting Times and Average Deposits')
fig.tight_layout()  # Verbessert das Layout

# Legende
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

plt.show()
