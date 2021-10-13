import os
import threading
from datetime import timedelta

from cam_recorder import CamRecorder
from config import single_url

threads = []

for i in range(4):
    cam_recorder = CamRecorder(
        url=single_url,
        filename=f'res{i}.avi',
        video_loop_size=timedelta(minutes=1)
    )
    thread = threading.Thread(target=cam_recorder.run)
    threads.append(thread)
    thread.start()


if __name__ == '__main__':
    if not os.path.exists('/media'):
        os.mkdir('/media')

    for thread in threads:
        thread.join()
