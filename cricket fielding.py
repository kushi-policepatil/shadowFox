import csv
import pandas as pd

FIELDING_CSV = "fielding_data.csv"

# Define field names
FIELDS = [
    'Over.Ball', 'Bowler', 'Batsman', 'Shot Type', 'Direction',
    'Fielder', 'Position', 'Action', 'Outcome', 'Runs Saved',
    'Runs Conceded', 'Wicket', 'Reaction Time', 'Throw Accuracy', 'Effort Level'
]

# Function to collect data for each ball
def collect_fielding_data():
    records = []
    num_entries = int(input("Enter number of balls to record: "))

    for _ in range(num_entries):
        print("\n--- Enter details for ball ---")
        record = {field: input(f"{field}: ") for field in FIELDS}
        records.append(record)

    return records


# Save data to CSV
def save_to_csv(records, filename=FIELDING_CSV):
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)

            # Write header only if file is empty
            file.seek(0)
            if not file.read(1):
                writer.writeheader()

            writer.writerows(records)

        print(f"\nData saved to {filename}")
    except Exception as e:
        print("Error saving file:", e)


# Basic analysis on the fielding data
def analyze_fielding(filename=FIELDING_CSV):
    try:
        df = pd.read_csv(filename)

        print("\n========== Fielding Performance Summary ==========")

        players = df['Fielder'].unique()
        for player in players:
            pdata = df[df['Fielder'] == player]

            total_actions = len(pdata)
            runs_saved = pdata['Runs Saved'].astype(int).sum()
            runs_conceded = pdata['Runs Conceded'].astype(int).sum()
            wickets = pdata['Wicket'].str.lower().eq('yes').sum()
            misfields = pdata['Action'].str.lower().eq('Missfield').sum()

            print(f"\nPlayer: {player}")
            print(f"Total Actions: {total_actions}")
            print(f"Runs Saved: {runs_saved}")
            print(f"Runs Conceded: {runs_conceded}")
            print(f"Wickets Contributed: {wickets}")
            print(f"Misfields: {misfields}")

        print("\n===================================================")

    except Exception as e:
        print("Error analyzing data:", e)


# Optional: Export to Excel
def export_to_excel(csv_file=FIELDING_CSV, excel_file='fielding_data.xlsx'):
    try:
        df = pd.read_csv(csv_file)
        df.to_excel(excel_file, index=False)
        print(f"\nData exported to {excel_file}")
    except Exception as e:
        print("Error exporting to Excel:", e)


# ----------- Main Program -----------
if __name__ == "__main__":
    while True:
        print("\n--- Cricket Fielding Data Collection ---")
        print("1. Record new fielding data")
        print("2. Analyze fielding performance")
        print("3. Export data to Excel")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = collect_fielding_data()
            save_to_csv(data)
        elif choice == '2':
            analyze_fielding()
        elif choice == '3':
            export_to_excel()
        elif choice == '4':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Try again.")
