# User Activity Aggregator

This repository contains code that reads a CSV file containing user activity logs, aggregates the data by user ID, and outputs the results in a JSON format.

### How to Run the Script

1.  **Navigate to the Script Directory**:
Open a terminal or command prompt and navigate to the directory containing the python script.

2.  **Run the Script**:
```bash
python script.py
```

### Dependencies

This script uses Python's standard library and does not require any additional dependencies:

### Brief Explanation of the Approach

1. **Reading and Aggregating Data**:
The read_and_aggregate_csv function reads the CSV file incrementally, processing each row to update aggregated data structures.

2. **Processing Each Row**:
The process_csv_row function updates activities, counts, timestamps, and IP addresses for each user, while avoiding missing values, incorrect format, and duplicate records.

3. **Writing to JSON**:
The write_json function saves the aggregated data to a JSON file.

### Assumptions:
This program is written for the input csv file having format - User ID,TimeStamp,Activity,Count,IP Address,Random String