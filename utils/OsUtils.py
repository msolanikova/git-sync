import os


class OsUtils:

    def norm(path):
        return os.path.normcase(os.path.normpath(path))
