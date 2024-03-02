from setuptools import Extension, setup
import platform

system = platform.system()

if system == 'Windows':
    setup(
        ext_modules=[
            Extension(
                name="cv2_enumerate_cameras._cv2_enumerate_cameras",
                sources=["src/cv2_enumerate_cameras/cv2_enumerate_cameras.cpp"]
            )
        ]
    )

if system == 'Linux':
    setup()
