import learn
from pipeline import get_pipeline
from predict import predict_proba, crossval, locations, predict
import time

def detect(loca):
    if 'third' in loca:
	    print("You're currently in B2, {}.".format(loca.replace("-", " ").title()))
    elif 'second' in loca:
	    print("You're currently in B2, {}.".format(loca.replace("-", " ").title()))
    elif 'first' in loca:
	    print("You're currently in B2, {}.".format(loca.replace("-", " ").title()))
    else:
        print("I don't know.")
while True:
    print("Detecting the location ...")
    location = predict()
    time.sleep(10)
    detect(location)