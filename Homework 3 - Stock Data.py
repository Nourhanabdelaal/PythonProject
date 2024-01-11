import os
import glob
import csv

folder_path = 'D:\\data'
output_folder = 'D:\\modified_files'

def search_csv_files(folder_path):
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    if not csv_files:
        print("No CSV files found in the specified folder.")
        return

    print("Found the following CSV files:")
    for csv_file in csv_files:
        print(csv_file)
        process_csv_file(csv_file)

def process_csv_file(csv_file):
    modified_rows = []

    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames + ['Change']

        for row in reader:
            close_price = float(row['Close'])
            open_price = float(row['Open'])

            change = ((close_price - open_price) / open_price) * 100

            row['Change'] = change
            modified_rows.append(row)

    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, os.path.basename(csv_file).replace('.csv', '_modified.csv'))

    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(modified_rows)

    print(f"Percentage change added to {csv_file}. Modified file saved to {output_file}")

search_csv_files(folder_path)
