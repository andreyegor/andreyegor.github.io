import os

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(script_dir, 'cv-ru-template.html'), 'r') as f:
    template = f.read()
with open(os.path.join(output_dir, 'cv-content.html'), 'r') as f:
    content = f.read()
result = template.replace('<!--CV_CONTENT_PLACEHOLDER-->', content)
with open(os.path.join(output_dir, 'index.html'), 'w') as f:
    f.write(result)

print("✓ index.html created in output/")

