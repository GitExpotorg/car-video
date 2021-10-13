import threading
from datetime import timedelta

from VideoRegistrator import CamRecorder
from config import single_url

# camera_urls = []
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

for thread in threads:
    thread.join()
