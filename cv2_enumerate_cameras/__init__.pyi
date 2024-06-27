from cv2_enumerate_cameras.camera_info import CameraInfo, CAP_ANY


supported_backends: tuple[int]


def enumerate_cameras(apiPreference: int = CAP_ANY) -> list[CameraInfo]:
    ...
