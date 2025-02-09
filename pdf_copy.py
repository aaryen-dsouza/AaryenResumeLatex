import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define multiple source directories
SOURCE_DIRS = {
    r"D:\Studies\Masters\CO-OP\AaryenResume\SD": "AaryenDSouza_SDResume.pdf",
    r"D:\Studies\Masters\CO-OP\AaryenResume\DE": "AaryenDSouza_DEResume.pdf"
}

# Define destination directory
DEST_DIR = r"D:\Studies\Masters\CO-OP\Current"
# Define log directory
LOG_DIR = r"D:\Studies\Masters\CO-OP\Logs"
LOG_FILE = os.path.join(LOG_DIR, "pdf_watch.log")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class PDFHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".pdf"):
            for src_dir, dest_filename in SOURCE_DIRS.items():
                if event.src_path.startswith(src_dir):
                    dest_path = os.path.join(DEST_DIR, dest_filename)
                    shutil.copy(event.src_path, dest_path)
                    log_message = f"Copied: {event.src_path} to {dest_path}"
                    print(log_message)
                    logging.info(log_message)
                    break

if __name__ == "__main__":
    event_handler = PDFHandler()
    observer = Observer()
    
    # Watch multiple directories
    for directory in SOURCE_DIRS.keys():
        observer.schedule(event_handler, directory, recursive=False)
    
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Observer stopped.")
    observer.join()
