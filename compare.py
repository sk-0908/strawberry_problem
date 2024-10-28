import csv
import os

def compare_csv_files(a_file, b_file, AI, times):
    discrepancies = []
    
    with    open(a_file, mode='r', encoding='utf-8') as file_a, \
            open(b_file, mode='r', encoding='utf-8') as file_b:
        
        reader_a = csv.reader(file_a)
        reader_b = csv.reader(file_b)

        for row_a, row_b in zip(reader_a, reader_b):
            if len(row_a) >= 3 and len(row_b) >= 3:  
                if row_a[2] != row_b[2]:
                    discrepancies.append(row_a[0])

    discrepancy_count = len(discrepancies)
    output_file = f'./result/{AI}/{AI}_{times}_{discrepancy_count}.csv'
    with open(output_file, mode='w', newline='', encoding='utf-8') as file_out:
        writer = csv.writer(file_out)
        for item in discrepancies:
            writer.writerow([item])

    print(f'異なる行の数: {discrepancy_count}, 出力ファイル: {output_file}')

if __name__ == "__main__":
    directory = os.path.dirname(__file__)

    #ここを変更する
    AI = 'example' 
    times = 0

    data_file_path = os.path.join(directory, 'strawberry_problem_test_data.csv')
    AI_file_path = os.path.join(directory, f"./answer/{AI}/{AI}_{times}.csv")
    
    compare_csv_files(data_file_path, AI_file_path, AI, times)
