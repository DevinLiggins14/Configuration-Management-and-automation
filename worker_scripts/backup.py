import os
import shutil
import tarfile
import datetime

# Configuration
BACKUP_SOURCE = ['/path/to/dir1', '/path/to/dir2']  # List of directories and files to back up
BACKUP_DESTINATION = '/path/to/backup/location'     # Backup destination directory

def create_backup(source_dirs, backup_dest):
    # Create a timestamped directory within the backup location
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_dir = os.path.join(backup_dest, f'backup_{timestamp}')
    
    try:
        os.makedirs(backup_dir, exist_ok=True)
    except Exception as e:
        print(f"Error creating backup directory: {e}")
        return
    
    # Create a .tar.gz archive of the specified directories and files
    backup_archive = os.path.join(backup_dir, f'backup_{timestamp}.tar.gz')
    
    try:
        with tarfile.open(backup_archive, 'w:gz') as tar:
            for source in source_dirs:
                if os.path.exists(source):
                    tar.add(source, arcname=os.path.basename(source))
                else:
                    print(f"Source path does not exist: {source}")
    except Exception as e:
        print(f"Error creating backup archive: {e}")
        return
    
    print(f"Backup successfully created at {backup_archive}")

def main():
    try:
        create_backup(BACKUP_SOURCE, BACKUP_DESTINATION)
    except Exception as e:
        print(f"Backup process encountered an error: {e}")

if __name__ == "__main__":
    main()
