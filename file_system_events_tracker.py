import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/Medhini/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def _on_created(self,event):
        print(f"Hey,{event.src_path} has been created!")

    def _on_deleted(self,event):
        print(f"Oops! someone deleted {event.src_path} !")  

    def _on_modified(self,event):
        print(f"Hey there!,{event.src_path} has been modified!") 

    def _on_moved(self,event):
        print(f"Someone moved,{event.src_path} to {event.dest_path}")
    

    

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()






