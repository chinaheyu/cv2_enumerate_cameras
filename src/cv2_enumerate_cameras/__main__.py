from . import enumerate_cameras, supported_backends
from .camera_info import CAP_ANY


try:
    from cv2.videoio_registry import getBackendName
except ModuleNotFoundError:
    def getBackendName(api):
        return str(api)


if __name__ == '__main__':
    for backend in [CAP_ANY, *supported_backends]:
        print(f'Enumerate using {getBackendName(backend)} backend:')
        for i in enumerate_cameras(backend):
            print(i)
        print()
