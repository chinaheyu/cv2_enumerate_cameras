from cv2_enumerate_cameras.camera_info import CameraInfo
import os
import glob

try:
    import cv2
    CAP_GSTREAMER = cv2.CAP_GSTREAMER
    CAP_V4L2 = cv2.CAP_V4L2
except ModuleNotFoundError:
    CAP_GSTREAMER = 1800
    CAP_V4L2 = 200

supported_backends = (CAP_GSTREAMER, CAP_V4L2)


def read_line(*args):
    try:
        with open(os.path.join(*args)) as f:
            line = f.readline().strip()
        return line
    except IOError:
        return None


def cameras_generator(apiPreference):
    for path in glob.glob('/dev/video*'):
        device_name = os.path.basename(path)
        index = int(device_name[5:])
        video_device_path = f'/sys/class/video4linux/{device_name}'
        usb_device_path = os.path.join(video_device_path, 'device')
        if os.path.exists(usb_device_path):
            usb_device_path = os.path.realpath(usb_device_path)
            if ':' in os.path.basename(usb_device_path):
                name = read_line(usb_device_path, 'interface')
                usb_device_path = os.path.dirname(usb_device_path)
            else:
                name = read_line(usb_device_path, 'product')
            vid = int(read_line(usb_device_path, 'idVendor'), 16)
            pid = int(read_line(usb_device_path, 'idProduct'), 16)
        else:
            name = read_line(video_device_path, 'name')
            vid = None
            pid = None
        if not name:
            name = device_name
        yield CameraInfo(index, name, path, vid, pid, apiPreference)


__all__ = ['supported_backends', 'cameras_generator']
