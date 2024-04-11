import pandas as pd

def excel_to_dict(excel_file: str) -> dict:

    df = pd.read_excel(excel_file)

    data_dict = df.to_dict('records')

    return data_dict

def write_to_excel(excel_file: str, tasks: dict) -> None:
    df = pd.read_excel(excel_file)

    start_dates = [tasks[task].start_date for task in tasks]
    end_dates = [tasks[task].end_date for task in tasks]

    df['start_date'] = pd.to_datetime(start_dates).date
    df['end_date'] = pd.to_datetime(end_dates).date

    output_file = 'updated_sheet.xlsx'

    df.to_excel(output_file, index=False)

    print("Data saved to", output_file)

if __name__ == "__main__":
    print(excel_to_dict("cult_project.xlsx"))
