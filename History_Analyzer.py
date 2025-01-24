# import os
#
# def analyze_history():
#     # Define the shell history file path (e.g., Bash history)
#     history_file = os.path.expanduser("~/.bash_history")  # Replace with ~/.zsh_history for Zsh
#
#     # Open the output file
#     with open("history_analytics_rpt", "w") as output_file:
#         # Read the history file
#         if os.path.exists(history_file):
#             with open(history_file, "r") as f:
#                 history_lines = f.readlines()
#
#             # Extract unique commands
#             commands = {}
#             for line in history_lines:
#                 line = line.strip()  # Remove leading/trailing whitespace
#                 if line:  # Only process non-empty lines
#                     command = line.split()[0]  # Get the first word (command)
#                     if command in commands:
#                         commands[command] += 1
#                     else:
#                         commands[command] = 1
#
#             # Write the command counts to the output file
#             for command, count in sorted(commands.items(), key=lambda x: x[1], reverse=True):
#                 output_file.write(f"{command}: {count}\n")
#
#             print("History analytics report generated: history_analytics_rpt")
#         else:
#             print(f"History file not found: {history_file}")
#
# # Run the function
# analyze_history()
