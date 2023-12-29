import json

with open('data/cname.md', 'r') as f:
    content = f.read()
markdown_content = content

# Split the markdown content into lines
lines = markdown_content.strip().split('\n')

# Filter out only the lines of the table (excluding headers and separators)
table_lines = [line for line in lines if '|' in line and '---' not in line]

# Process each line of the table
company_list = []
for line in table_lines:
    # Extract the columns of the table
    columns = [col.strip() for col in line.split('|') if col.strip()]
    company_list.append(columns)

# Convert dictionary to JSON
json_output = json.dumps(company_list, indent=2, ensure_ascii=False)

with open('output/cname.json', 'w') as f:
    f.write(json_output)
