import json
import csv

# JSON 파일 경로 지정
json_file_path = 'data_processing/recipes_metadata.json'
# CSV 파일 경로 지정
csv_file_path = 'data/ingredients.csv'

# JSON 파일 읽기
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# CSV 파일로 쓰기
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    # 필드 이름 설정 (recipe 테이블에 맞춤)
    fieldnames = ['recipe_id', 'recipe_ingredient']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        # 필요한 필드만 추출하고 필드 이름에 맞게 매핑
        row = {
            'recipe_id': item['recipe_no'],
            'recipe_ingredient': item['recipe_ingredient']
        }
        writer.writerow(row)

print("JSON to CSV conversion completed successfully.")
