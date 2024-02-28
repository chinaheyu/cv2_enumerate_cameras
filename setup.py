from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="cv2_enumerate_cameras._cv2_enumerate_cameras",
            sources=["src/cv2_enumerate_cameras/cv2_enumerate_cameras.cpp"]
        )
    ]
)
