import pandas as pd

def validate_data(df):
    print("=" * 50)
    print("DATA VALIDATION REPORT")
    print("=" * 50)

    # Missing values
    print("\nMissing Values")
    print(df.isnull().sum())

    # Duplicate rows
    duplicates = df.duplicated().sum()
    print("\nDuplicate Rows:", duplicates)

    # Data types
    print("\nData Types")
    print(df.dtypes)

    # Invalid values - these checks are not directly applicable to the scaled and encoded df_selected
    # invalid_age = (df["age"] <= 0).sum()
    # invalid_bp = (df["trestbps"] <= 0).sum()

    # print("\nInvalid Age:", invalid_age)
    # print("Invalid Blood Pressure:", invalid_bp)

    print("\nValidation Completed Successfully")

if __name__ == "__main__":
    # The 'df_selected' DataFrame is available in the global scope from previous executions.
    # We can directly pass it to the validation function instead of reading from a file.
    validate_data(df_selected)
