import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Hypothetisches Einlesen der Daten
data = pd.read_csv('DuneMaster.csv')

# Umwandlung der 'block_time' in ein Datum im Format YYYY-MM-DD
data['date'] = pd.to_datetime(data['block_time']).dt.date

# Berechnung des ETH-Preises für jede Transaktion
data['eth_price'] = data['deposit_usd'] / data['deposit_eth']

# Filtern der Daten auf Einsätze, die nicht in ETH getätigt wurden
non_eth_bets = data[data['collateral_name'] != 'ETH']

# Berechnen der Anzahl der Einsätze mit allem außer ETH pro Tag
non_eth_bets_per_day = non_eth_bets.groupby('date').size()

# Berechnung des durchschnittlichen ETH-Preises pro Tag für alle Transaktionen
average_eth_price_per_day = data.groupby('date')['eth_price'].mean()

# Erstellen des Plots
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Datum')
ax1.set_ylabel('Anzahl an Einsätzen mit allem außer ETH', color=color)
ax1.plot(non_eth_bets_per_day.index, non_eth_bets_per_day, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Zweite Y-Achse für den durchschnittlichen ETH-Preis
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Durchschnittlicher ETH-Preis', color=color)
ax2.plot(average_eth_price_per_day.index, average_eth_price_per_day, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Formatierung des Datums auf der X-Achse
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

fig.tight_layout()  # adjust layout
plt.title('Anzahl an Einsätzen mit allem außer ETH und ETH-Preisverlauf')
plt.show()
