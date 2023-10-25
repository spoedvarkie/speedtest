# Function definitions
import datetime
from pathlib import Path


def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return "int"
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float number not integer")
            return "float"
        except ValueError:
            print("Input is a string not integer - checking date")
            try:
                date_timestamp = datetime.datetime.strptime(input, "%d/%m/%Y %H:%M")
                print("Date is good")
                return "date"
            except ValueError:
                print("Input is not a date either")
                return "false"


def file_exists(file_path_name):
    my_file = Path(file_path_name)
    if my_file.is_file():
        return True
    else:
        return False


def write_results(result_list: list):
    if not file_exists("results.csv"):
        header = ['time', 'curr_run', 'curr_duration', 'curr_ping', 'curr_upload', 'curr_download', 'total_duration',
                  'total_sent', 'total_received', 'avg_duration', 'avg_ping', 'avg_upload_speed', 'avg_download_speed']
        with open('results.csv', 'w', encoding='UTF8') as f:
            f.write(','.join(map(str, header)))
            for r in range(len(result_list)):
                f.write("\n")
                f.write(','.join(map(str, result_list[r])))
            f.close()
    else:
        with open('results.csv', 'a', encoding='UTF8') as f:
            for r in range(len(result_list)):
                f.write("\n")
                f.write(','.join(map(str, result_list[r])))
            f.close()
