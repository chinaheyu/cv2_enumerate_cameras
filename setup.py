from setuptools import Extension, setup
import platform

system = platform.system()

if system == 'Windows':
    setup(
        ext_modules=[
            Extension(
                name="cv2_enumerate_cameras._windows_backend",
                sources=["src/cv2_enumerate_cameras/_windows_backend.cpp"]
            )
        ]
    )

if system == 'Linux':
    setup()
