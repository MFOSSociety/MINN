import time
import json
from tqdm import tqdm
from get_data import sample
from pipeline import train_model
from utils import ensure_model_path, get_label_file

def write_data(label_path, data):
    with open(label_path, "a") as f:
        f.write(json.dumps(data))
        f.write("\n")

def learn(label, n=1, device=""):
    path = ensure_model_path()
    label_path = get_label_file(path, label + ".txt")
    for i in tqdm(range(n)):
        if i != 0:
            time.sleep(15)
        try:
            new_sample = sample(device)
            if new_sample:
                write_data(label_path, new_sample)
        except KeyboardInterrupt:
            break
    train_model()
