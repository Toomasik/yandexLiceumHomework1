def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def get_db_path():
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
        local_db = os.path.join(base_dir, "coffee.db")
        if not os.path.exists(local_db):
            bundled_db = resource_path("data/coffee.db")
            shutil.copyfile(bundled_db, local_db)
        return local_db
    else:
        return resource_path("data/coffee.db")

DB_PATH = get_db_path()