import learn
from pipeline import get_pipeline
from predict import predict_proba, crossval, locations, predict
import time

LOCATIONS = ['first', 'second', 'third']


def detect(loca):
	for location_ in LOCATIONS:
		if location_ in loca:
			print("You're currently in B2, {}.".format(loca.replace("-", " ").title()))
			return None

	print("I don't know.")


while True:
	print("Detecting the location ...")
	location = predict()
	time.sleep(10)
	detect(location)
