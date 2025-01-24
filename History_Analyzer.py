import os
import subprocess

def get_command_description(command):
    """
    Get the description of a command using the 'whatis' command.
    If no description is found, return 'No description available'.
    """
    try:
        whatis_output = subprocess.check_output(f"whatis {command}", shell=True, text=True).strip()
        return whatis_output
    except subprocess.CalledProcessError:
        return "No description available"

def analyze_history():
    """
    Analyze the shell history file and generate a report with command counts and descriptions.
    """
    # Define the shell history file path (e.g., Bash history)
    history_file = os.path.expanduser("~/.bash_history")  # Replace with ~/.zsh_history for Zsh

    # Define the output file name
    output_file = "history_analytics_rpt"

    # Open the output file
    with open(output_file, "w") as f:
        # Read the history file
        if os.path.exists(history_file):
            with open(history_file, "r") as history:
                history_lines = history.readlines()

            # Extract unique commands and their counts
            command_counts = {}
            for line in history_lines:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:  # Only process non-empty lines
                    command = line.split()[0]  # Get the first word (command)
                    if command in command_counts:
                        command_counts[command] += 1
                    else:
                        command_counts[command] = 1

            # Write header row with improved formatting
            f.write(f"{'Command':<15}{'Count':<10}{'Description'}\n")
            f.write(f"{'-' * 70}\n")

            # Write command details with improved alignment
            for command, count in sorted(command_counts.items(), key=lambda x: x[1], reverse=True):
                description = get_command_description(command)
                f.write(f"{command:<15}{count:<10}{description}\n")

            print(f"History analytics report generated: {output_file}")
        else:
            print(f"History file not found: {history_file}")

# Run the function
if __name__ == "__main__":
    analyze_history()
