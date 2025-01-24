import pandas as pd
import matplotlib.pyplot as plt

# Read the report file
report_file = "history_analytics_rpt"
data = []

# Open the report and process it
with open(report_file, "r") as f:
    lines = f.readlines()
    for line in lines[2:]:  # Skip header
        command, count_desc = line.split(": ")
        count_desc_parts = count_desc.split(", Description: ")

        # Handle lines with or without the description part
        if len(count_desc_parts) == 2:
            count, desc = count_desc_parts
        else:
            count = count_desc_parts[0]  # Just count if no description
            desc = "No description available"  # Default description

        data.append([command.strip(), int(count.strip()), desc.strip()])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Command", "Count", "Description"])

# Handle missing descriptions (optional, this can be adjusted based on your needs)
df['Description'] = df['Description'].apply(lambda x: x if x != "No description available" else "No description available")

# Display first few rows to check
print(df.head())

# Visualization: Plot the most common commands
plt.figure(figsize=(10, 6))
top_commands = df.nlargest(10, 'Count')  # Get the top 10 commands
plt.barh(top_commands['Command'], top_commands['Count'], color='skyblue')
plt.xlabel('Command Frequency')
plt.title('Top 10 Commands in Bash History')
plt.gca().invert_yaxis()  # To show the highest count at the top
plt.show()

# Optionally, save the DataFrame to a CSV for further analysis
df.to_csv("history_analytics_report.csv", index=False)
