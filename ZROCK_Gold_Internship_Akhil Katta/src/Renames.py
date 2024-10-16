import os

def rename_file(old_name, new_name):
    try:
        
        os.rename(old_name, new_name)
        print(f"File renamed from {old_name} to {new_name}")
    except FileNotFoundError:
        print(f"File {old_name} not found!")
    except PermissionError:
        print(f"Permission denied while renaming {old_name}!")
    except Exception as e:
        print(f"An error occurred: {e}")


old_file_name = 'Akhil_file.txt'
new_file_name = 'Raju_file.txt'
rename_file(old_file_name, new_file_name)

