import csv
import json
from collections import defaultdict
from datetime import datetime

def process_csv_row(row, output_data, seen_records):
    """
    Processes a single row of CSV data and updates the aggregated data.
    """
    valid_row = True
    # Ensure valid timestamp format
    try:
        row['TimeStamp'] = datetime.strptime(row['TimeStamp'], '%Y-%m-%d %H:%M:%S')
    except (ValueError, TypeError):
        valid_row = False

    # check for other valid row values
    valid_row = True if (row['User ID'] and row['Random String'] and row['Activity'] and row['Count'] and row['Count'].isdigit() and row['IP Address']) else False

    if not valid_row:
        print(f"Invalid format for row: {row}")
        return

    user_id = row['User ID']
    random_string = row['Random String']
    
    # Skip duplicate records
    if random_string in seen_records:
        return
    
    seen_records.add(random_string)
    
    output_data[user_id]['activities'].append(row['Activity'])
    output_data[user_id]['total_count'] += int(row['Count'])
    output_data[user_id]['timestamps'].append(row['TimeStamp'].strftime('%Y-%m-%d %H:%M:%S'))
    output_data[user_id]['ip_addresses'].add(row['IP Address'])

def read_and_aggregate_csv(file_path):
    """
    Reads the CSV file and aggregates data by User ID.
    """
    output_data = defaultdict(lambda: {'activities': [], 'total_count': 0, 'timestamps': [], 'ip_addresses': set()})
    seen_records = set()

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:                
                process_csv_row(row, output_data, seen_records)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")

    # Convert sets to lists for JSON serialization
    for user_id in output_data:
        output_data[user_id]['ip_addresses'] = list(output_data[user_id]['ip_addresses'])
    
    return output_data

def write_json(data, file_path):
    """
    Writes the aggregated data to a JSON file.
    """
    try:
        with open(file_path, mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)
    except Exception as e:
        print(f"An error occurred while writing the JSON file: {e}")

def main():
    input_file = 'user_activities.csv'                  # input file name; should be there in the same directory as of script.py
    output_file = 'aggregated_activities.json'      # output file name; saves in the same directory as of script.py
    
    output_data = read_and_aggregate_csv(input_file)
    if not output_data:
        print("No valid data to process!!")
        return
    
    write_json(output_data, output_file)
    print(f"Successfully written data to {output_file}")

if __name__ == "__main__":
    main()
