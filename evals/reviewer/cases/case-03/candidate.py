def sync(mode, backup, write):
    if mode not in ("install", "check"):
        raise ValueError("unsupported mode")
    if mode == "check":
        return 0
    backup()
    write()
    return 0
