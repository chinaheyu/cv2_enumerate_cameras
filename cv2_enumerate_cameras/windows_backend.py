from cv2_enumerate_cameras.camera_info import CameraInfo
from cv2_enumerate_cameras._windows_backend import MSMF_enumerate_cameras, DSHOW_enumerate_cameras
import re


try:
    import cv2
    CAP_MSMF = cv2.CAP_MSMF
    CAP_DSHOW = cv2.CAP_DSHOW
except ModuleNotFoundError:
    CAP_MSMF = 1400
    CAP_DSHOW = 700

supported_backends = (CAP_MSMF, CAP_DSHOW)


def cameras_generator(apiPreference):
    def parse_vid_pid(path):
        if path:
            m = re.search(r'vid_([0-9a-f]{4})&pid_([0-9a-f]{4})', path, re.IGNORECASE)
            if m:
                return int(m.group(1), 16), int(m.group(2), 16)
        return None, None

    camera_list = None
    if apiPreference == CAP_MSMF:
        camera_list = MSMF_enumerate_cameras()
    if apiPreference == CAP_DSHOW:
        camera_list = DSHOW_enumerate_cameras()

    if camera_list is not None:
        for index, (name, path) in enumerate(camera_list):
            vid, pid = parse_vid_pid(path)
            yield CameraInfo(index, name, path, vid, pid, apiPreference)


__all__ = ['supported_backends', 'cameras_generator']
