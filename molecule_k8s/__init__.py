try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution('molecule-k8s').version
except Exception:  # pragma: no cover
    __version__ = 'unknown'
