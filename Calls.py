# Function definitions
from pathlib import Path


def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float number not integer")
            return False
        except ValueError:
            print("Input is not a string not integer")
            return False


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
    else:
        with open('results.csv', 'a', encoding='UTF8') as f:
            for r in range(len(result_list)):
                f.write("\n")
                f.write(','.join(map(str, result_list[r])))
