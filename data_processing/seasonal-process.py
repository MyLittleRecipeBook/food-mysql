import csv

# 원본 CSV 파일 경로
input_csv_path = 'seasonal.csv'
# 가공된 CSV 파일 경로
output_csv_path = 'seasonal_process.csv'

# 필요한 필드만 추출하여 가공
with open(input_csv_path, 'r', encoding='utf-8') as infile, open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['seasonal_name', 'seasonal_month', 'seasonal_image']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in reader:
        # 월별 필드에서 "월" 제거하고 숫자만 추출
        seasonal_month = row['월별'].replace('월', '')
        writer.writerow({
            'seasonal_name': row['품목명'],
            'seasonal_month': seasonal_month,
            'seasonal_image': row['이미지 URL']
        })

print("CSV data processed and saved to", output_csv_path)
