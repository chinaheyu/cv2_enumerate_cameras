# type: ignore
from cv2_enumerate_cameras import enumerate_cameras, supported_backends
from cv2_enumerate_cameras.camera_info import CAP_ANY


try:
    from cv2.videoio_registry import getBackendName
except ModuleNotFoundError:
    def getBackendName(api):
        return str(api)


def main():
    for backend in [CAP_ANY, *supported_backends]:
        print(f'Enumerate using {getBackendName(backend)} backend:')
        camera_infos = enumerate_cameras(backend)
        name_column_length = max((len(i.name) for i in camera_infos))
        path_column_length = max((len(i.path) for i in camera_infos))

        separate_line = "+-------+-" + "-" * name_column_length + "-+------+------+-" + "-" * path_column_length + "-+"
        output_rows = [
            separate_line,
            "| index | " + "name".center(name_column_length) + " | vid  | pid  | " + "path".center(path_column_length) + " |",
            separate_line
        ]
        for i in camera_infos:
            row = f"| {i.index:5} | {i.name:{name_column_length}} | "
            if i.vid is None:
                row += f" --  | "
            else:
                row += f"{i.vid:04X} | "
            if i.pid is None:
                row += f" --  | "
            else:
                row += f"{i.pid:04X} | "
            row += f"{i.path:{path_column_length}} |"
            output_rows.append(row)
        output_rows.append(separate_line)
        print('\n'.join(output_rows))


if __name__ == '__main__':
    main()
