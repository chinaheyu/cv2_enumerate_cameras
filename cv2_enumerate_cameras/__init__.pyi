from cv2_enumerate_cameras.camera_info import CameraInfo


supported_backends: tuple[int]


def enumerate_cameras(apiPreference: int = ...) -> list[CameraInfo]:
    ...
