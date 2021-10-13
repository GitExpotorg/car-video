import os
from datetime import timedelta

from cam_recorder import CamRecorder
from config import single_url, camera_urls_names


if __name__ == '__main__':
    if not os.path.exists('media'):
        os.mkdir('media')

    for url, name in camera_urls_names:
        cam_recorder = CamRecorder(
            url=url,
            filename=f'res:{name}.avi',
            video_loop_size=timedelta(minutes=1)
        )
        cam_recorder.start()
