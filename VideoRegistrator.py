from datetime import datetime, timedelta

import cv2

from config import logger, single_url


class CamRecorder:
    def __init__(self, url: str, filename: str, video_loop_size: timedelta):
        self.cap = cv2.VideoCapture(url)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.filename = filename
        self.image_size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # self.image_size = (1366, 768)
        self.out = None
        self.loop_time_in_seconds = int(video_loop_size.total_seconds()) * self.fps

    def check_capture(self):
        return self.cap.isOpened()

    def run(self):
        try:
            if self.check_capture():
                logger.info(f'Start recording')
                while True:
                    datetime_now = datetime.now()
                    datetime_string = f'{datetime_now.date()}_{datetime_now.hour:02d}:' \
                                      f'{datetime_now.minute:02d}:{datetime_now.second:02d}'

                    self.out = cv2.VideoWriter(f'media/{datetime_string}_{self.filename}',
                                               cv2.VideoWriter_fourcc(*'XVID'),
                                               self.fps,
                                               self.image_size,
                                               True)

                    for i in range(self.loop_time_in_seconds):
                        ret, frame = self.cap.read()
                        # frame = cv2.resize(frame, self.image_size, interpolation=cv2.INTER_LINEAR)
                        self.out.write(frame)
                    else:
                        logger.info(f'file "{datetime_string}_{self.filename}" has been recorded')

        except KeyboardInterrupt:
            logger.info('Recording stopped by user')
        except Exception as e:
            logger.warning(f'Some error occurred: {e}')
        finally:
            self.cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    cam_recorder = CamRecorder(
        url=single_url,
        filename='res.avi',
        video_loop_size=timedelta(minutes=1)
    )
    cam_recorder.run()
