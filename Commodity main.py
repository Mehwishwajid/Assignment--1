import pandas as pd
import  matplotlib.pyplot as plt
import matplotlib.ticker as ticker
file_name = 'commodity_trade_statistics_data.csv'
pd.set_option('display.max_columns', None)
data = pd.read_csv(file_name, encoding='latin1')
print(data)

'''def  TradeProgress(data):
    selected_countries = ['USA', 'Spain', 'France']
    filtered_data = data[data['country_or_area'].isin(selected_countries)]
    grouped_data = filtered_data.groupby(['country_or_area', 'year'])['trade_usd'].sum().reset_index()
    plt.figure(figsize=(12, 6))
    for country in selected_countries:
        country_data = grouped_data[grouped_data['country_or_area'] == country]
        plt.plot(country_data['year'], country_data['trade_usd'], label=country)

    plt.xlabel('Year')
    plt.ylabel('Total Trade (in USD)')
    plt.title('Trade Comparsion Between USA , Spain and France Over the Years')
    plt.legend(loc='best')
    plt.grid(True)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.0f}'.format(x)))
    plt.show()
    
    
TradeProgress(data)'''


'''def top_exporting_countries(data):
    export_data = data[data['flow'] == 'Export']
    country_totals = export_data.groupby('country_or_area')['trade_usd'].sum().reset_index()
    top_countries = country_totals.sort_values(by='trade_usd', ascending=False).head(5)
    plt.figure(figsize=(8, 8))
    plt.pie(top_countries['trade_usd'], labels=top_countries['country_or_area'], autopct='%1.1f%%')
    plt.title('Top 5 Countries in Exports')
    plt.show()


top_exporting_countries(data)'''

'''def flow_bar_graph(data):

  exports = data[data["flow"] == "Export"]
  imports = data[data["flow"] == "Import"]


  total_exports = exports["trade_usd"].sum()
  total_imports = imports["trade_usd"].sum()

  # Create a bar graph
  fig, ax = plt.subplots()
  bar_width = 0.35
  index = [0, 1]
  bar1 = ax.bar(index[0], total_exports, bar_width, label="Exports")
  bar2 = ax.bar(index[1], total_imports, bar_width, label="Imports")

  # Set the labels and title
  ax.set_xlabel("Flow")
  ax.set_ylabel("Total Trade USD")
  ax.set_title("Total Trade USD by Flow")

  # Set the x-axis ticks
  ax.set_xticks(index)
  ax.set_xticklabels(["Exports", "Imports"])

  # Add a legend
  ax.legend()

  # Show the plot
  plt.show()


flow_bar_graph(data)'''













