import pandas as pd


def dataframe(csv):
    df = file_path_cleaner(csv)
    df = read_csv(df)
    return df


def read_csv(csv):
    csv = pd.read_csv(csv)
    return csv


def print_csv(df):
    print(df)


def get_columns(df):
    column_names = df.dtypes

    return column_names


def file_path_cleaner(file_path):
    c_file_path = file_path.replace('\\', "/")
    return c_file_path


def get_dataframe():
    filepath = file_path_cleaner('C:\\Users\Garrett '
                     'Bousquet\Desktop\covidproj\united_states_covid_cases_deaths_and_testing_by_state.csv')

    dataf = read_csv(filepath)
    return dataf


print(get_columns(get_dataframe()))
