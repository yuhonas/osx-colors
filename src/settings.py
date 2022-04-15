from importlib.metadata import version

APP_NAME = "osx-colors"  # TODO: Can we get this from the package meta data?


def get_version():
    return version(APP_NAME)


def get_app_name():
    return APP_NAME
