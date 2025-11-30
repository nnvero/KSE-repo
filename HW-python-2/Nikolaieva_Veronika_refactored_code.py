import pandas as pd

AGE_THRESHOLD = 50

def load_data(file_path):
    """
    Load data from the file

    Input: path of a .csv file as string
    Output: pd.DataFrame
    """
    data = pd.read_csv(file_path)
    return data

def find_responsive_patients(df):
    """
    Find patients whosw age is above 50 with lung cancer and whose 
    tumor size is decreased compared to baseline 

    Input: pd.DataFrame
    Output: list of strings
    """
    filtered = df[
        (df["age"] >= AGE_THRESHOLD) &
        (df["cancer_type"] == "Lung") &
        (df["final_tumor_size"] < df["baseline_tumor_size"])
    ]

    return filtered["patient_id"].tolist()

def calculate_survival_means(df):
    """
    Calculate survival means per trearment group

    Input: pd.DataFrame
    Output: pd.Series
    """
    grouped_data = df.groupby("treatment")
    mean_values = grouped_data["survival_months"].mean()

    return mean_values

def analyze_data(file_path):
    """
    Coordinates functions to load data, find redponsive patients
    and cumpute survival statistics

    Input: path of a .csv file as string
    Output: list of strings
    """
    df = load_data(file_path)
    responsive_patients = find_responsive_patients(df)
    survival_means = calculate_survival_means(df)

    print("Average survival by treatment:")
    print(survival_means)

    print("Number of responsive patients:", len(responsive_patients))

    return responsive_patients


analyzis = analyze_data("clinical_trial_patients.csv")