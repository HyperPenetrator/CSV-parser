import csv

def parse_csv(filename):
    features = []
    labels = []

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header row

            for row in reader:
                # Last column as label, rest as features
                features.append([float(x) for x in row[:-1]])
                labels.append(row[-1])
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"Error while parsing: {e}")
    
    return features, labels
