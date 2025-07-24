import os

# Define project structure
folders = [
    "app", "app/static", "app/templates", "app/models", "app/routes",
    "tests", "migrations"
]
files = [
    "app/__init__.py", "app/models.py", "app/routes.py", "app/config.py",
    "run.py", "requirements.txt", ".env"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    open(file, 'w').close()

print("Flask project structure created successfully!")
