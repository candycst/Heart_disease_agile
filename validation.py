import pandas as pd

def validate_data(df):
    print("=" * 50)
    print("DATA VALIDATION REPORT")
    print("=" * 50)

    # 1. Missing values
    print("\n1. Missing Values")
    print(df.isnull().sum())

    # 2. Duplicate rows
    duplicates = df.duplicated().sum()
    print("\n2. Duplicate Rows:", duplicates)

    # 3. Data types
    print("\n3. Data Types")
    print(df.dtypes)

    # 4. Invalid values
    print("\n4. Invalid Values")

    if "age" in df.columns:
        invalid_age = (df["age"] <= 0).sum()
        print("Invalid Age:", invalid_age)

    if "trestbps" in df.columns:
        invalid_bp = (df["trestbps"] <= 0).sum()
        print("Invalid Resting Blood Pressure:", invalid_bp)

    if "chol" in df.columns:
        invalid_chol = (df["chol"] <= 0).sum()
        print("Invalid Cholesterol:", invalid_chol)

    print("\n")
    print("=" * 50)
    print("Validation Completed Successfully")
    print("=" * 50)


if __name__ == "__main__":
    # Load your dataset
    df = pd.read_csv("heart_disease_uci.csv")

    # Run validation
    validate_data(df)
