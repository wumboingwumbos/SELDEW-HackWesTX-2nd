import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# Read the CSV data into a list of dictionaries
filename = 'data.csv'  # Replace with the actual path to your CSV file
data = []

with open(filename, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append(row)

# Function to sum water usage by date and group by either Name or Location
def get_water_usage_by_date_and_group(data, group_by):
    usage_by_date = defaultdict(lambda: defaultdict(int))

    for row in data:
        group = row[group_by]  # Either 'Name' or 'Location'
        date = row['Date']
        usage_by_date[date][group] += int(row['Water Use Duration (in Seconds)'])

    return usage_by_date

# Function to sum water usage by date for a specific name
def get_water_usage_for_one_user(data, target):
    usage_by_date = defaultdict(int)

    for row in data:
        group = row['Name']
        if group.lower() == target.lower():  # Case-insensitive comparison
            date = row['Date']
            usage_by_date[date] += int(row['Water Use Duration (in Seconds)'])

    return usage_by_date

# Plot the water usage in a bar chart (grouped by Name or Location)
def plot_water_usage(usage_by_date, group_by, filename=None):
    dates = list(usage_by_date.keys())
    groups = list(set(group for date in usage_by_date for group in usage_by_date[date]))

    # Define width for bars and figure layout
    bar_width = 0.8 / len(groups)  # Adjust width based on number of groups
    fig, ax = plt.subplots(figsize=(12, 8))

    # Generate the bar chart for each group (name or location)
    indices = range(len(dates))

    for i, group in enumerate(groups):
        group_durations = [usage_by_date[date].get(group, 0) for date in dates]
        bar_positions = [x + i * bar_width for x in indices]
        ax.bar(bar_positions, group_durations, bar_width, label=group)

    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Water Use Duration (Seconds)')
    ax.set_title(f'Water Usage by {group_by.capitalize()} and Date')
    ax.set_xticks([x + bar_width * (len(groups) - 1) / 2 for x in indices])
    ax.set_xticklabels(dates, rotation=45)
    ax.legend(title=group_by.capitalize())

    # Display the plot or save as PNG
    if filename:
        plt.savefig(filename, format='png')
        print(f"Graph saved as {filename}")
    else:
        plt.tight_layout()
        plt.show()

    # Close the plot to allow the program to continue
    plt.close()

  # Plot the water usage in a bar chart for a specific user
def plot_water_usage_for_one(usage_by_date, target, filename=None):
      dates = list(usage_by_date.keys())
      durations = list(usage_by_date.values())

      # Define figure layout
      fig, ax = plt.subplots(figsize=(12, 8))

      # Generate the bar chart
      ax.bar(dates, durations, width=0.5, label=target)

      # Set labels and title
      ax.set_xlabel('Date')
      ax.set_ylabel('Water Use Duration (Seconds)')
      ax.set_title(f'Water Usage for {target} by Name and Date')
      ax.set_xticks(dates)
      ax.set_xticklabels(dates, rotation=45)
      ax.legend(title='Name')

      # Display the plot or save as PNG
      if filename:
          plt.savefig(filename, format='png')
          print(f"Graph saved as {filename}")
      else:
          plt.tight_layout()
          plt.show()

      # Close the plot to allow the program to continue
      plt.close()

          # Function to select the graph type
def select_graph(type, target=None, filename=None):
              if type == 'name_grouped':
                  # Get the aggregated water usage by date and group by Name
                  usage_by_date_and_group = get_water_usage_by_date_and_group(data, 'Name')
                  # Plot the bar graph and save it
                  plot_water_usage(usage_by_date_and_group, 'Name', filename)

              elif type == 'location_grouped':
                  # Get the aggregated water usage by date and group by Location
                  usage_by_date_and_group = get_water_usage_by_date_and_group(data, 'Location')
                  # Plot the bar graph and save it
                  plot_water_usage(usage_by_date_and_group, 'Location', filename)

              elif type == 'specific_user':
                  # Get the water usage for the specific user
                  usage_by_date_for_one = get_water_usage_for_one_user(data, target)
                  # Plot the bar graph for the specific user and save it
                  if usage_by_date_for_one:
                      plot_water_usage_for_one(usage_by_date_for_one, target, filename)
                  else:
                      print(f"No data available for {target}.")

# To save the graph grouped by name as 'name_grouped.png'
select_graph('name_grouped', filename='name_grouped.png')

# To save the graph grouped by location as 'location_grouped.png'
select_graph('location_grouped', filename='location_grouped.png')

# To save the graph for a specific user (e.g., 'Leo') as 'specifieduser_usage.png'
select_graph('specific_user', target='Leo', filename='specific user_usage.png')
