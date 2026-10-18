def sync(mode, backup, write):
    if mode == "collect":
        raise ValueError("unsupported mode")
    if mode == "install":
        backup()
    write()
    return 0
