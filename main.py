from controllers import Youtube_viewer
from time import sleep
import sqlite3

if __name__ == '__main__':
    controller = Youtube_viewer()
    controller.open_recent_YT_video()