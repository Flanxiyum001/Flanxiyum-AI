import os

# Folder structure
folders = [
    "project_folder/templates",
    "project_folder/static/css",
    "project_folder/static/js"
]

# Create directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
files = [
    "project_folder/templates/index.html",
    "project_folder/static/css/style.css",
    "project_folder/static/js/script.js",
    "project_folder/app.py"
]

for file in files:
    with open(file, 'w') as f:
        pass  # Just create the empty file

print("Folder structure and files created successfully!")
