from Fold.source.parse import parse_csv

def main():
    filename = 'data/sample_train.csv'
    features, labels = parse_csv(filename)

    print("📦 Features:")
    for f in features:
        print(f)

    print("\n🏷️ Labels:")
    for l in labels:
        print(l)

if __name__ == '__main__':
    main()
