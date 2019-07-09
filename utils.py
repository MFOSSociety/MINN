import os

def get_model_path(path=None):
    if path is None:
        path = os.path.join(os.getcwd(), os.path.basename('dataset'))
    return os.path.expanduser(path)

def ensure_model_path():
    path = get_model_path()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_model_file(path=None, model="model.pkl"):
    path = ensure_model_path() if path is None else path
    return os.path.join(path, model)

def get_label_file(path, label):
    return os.path.join(get_model_path(path), label)

def rename_label(label, new_label, path=None):
    path = ensure_model_path() if path is None else path
    from_path = os.path.join(path, label + ".txt")
    new_path = os.path.join(path, new_label + ".txt")
    os.rename(from_path, new_path)
    print("Renamed {} to {}".format(from_path, new_path))
