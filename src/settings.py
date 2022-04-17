import importlib.metadata as importlib_metadata

APP_NAME = "osx-colors"  # TODO: Can we get this from the package meta data?


def get_version():
    try:
        version = importlib_metadata.version(APP_NAME)
    except importlib_metadata.PackageNotFoundError:
        version = "0.0.0"  # FIXME: No package to get a version from, we're probably in dev

    return version


def get_app_name():
    return APP_NAME
