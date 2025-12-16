import shutil

def backup_database():
    shutil.copy("finance.db", "finance_backup.db")

def restore_database():
    shutil.copy("finance_backup.db", "finance.db")
