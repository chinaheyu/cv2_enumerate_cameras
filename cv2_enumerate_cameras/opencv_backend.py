from cv2_enumerate_cameras.camera_info import CameraInfo
import cv2


supported_backends = cv2.videoio_registry.getCameraBackends()


def parse_frame_format(frame_format):
    type_list = ['8U', '8S', '16U', '16S', '32S', '32F', '64F']
    if not isinstance(frame_format, int):
        frame_format = int(frame_format)
    if frame_format == -1:
        return ""
    return type_list[frame_format % 8] + f'C{frame_format // 8 + 1:d}'


def cameras_generator(apiPreference):
    log_level = cv2.getLogLevel()
    cv2.setLogLevel(0)
    for camera_index in range(100):
        camera = cv2.VideoCapture(camera_index, apiPreference)
        if camera.isOpened():
            width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
            fps = camera.get(cv2.CAP_PROP_FPS)
            frame_format = parse_frame_format(camera.get(cv2.CAP_PROP_FORMAT))
            yield CameraInfo(camera_index, f'video_{width:.0f}x{height:.0f}_{frame_format}_{fps:.2f}_{camera_index}', None, None, None, apiPreference)
    cv2.setLogLevel(log_level)


__all__ = ['supported_backends', 'cameras_generator']
