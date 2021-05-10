# MINN

<p align="center">
<b>Wi-Fi indoor positioning system for Manipal University Jaipur.</b><br><br>
    <img alt="MINN logo" src="static/minn-logo.png" width="400"><br>
<b>Works without Internet/GPS/Anything!<br>
  Click <a href="#Demo">here</a> to see the demo.<br><br></b>
</p>

## Why this Project (?)

An indoor positioning system (IPS) is a network of devices used to locate people or objects where GPS and other satellite technologies lack precision or fail entirely, such as inside multistory buildings, airports, alleys, parking garages, and underground locations because the signals can be easily blocked by aforementioned structures making it useless for such environments because of signal loss.

Global navigation satellite systems (GPS or GNSS) which remain the most prevalent and well-known technology for locating and tracking entities outdoors are generally not suitable to establish indoor locations, since microwaves will be attenuated and scattered by roofs, walls and other objects. Building a three dimensional (3d) map of the whole university is a difficult job. However, in order to make positioning signals ubiquitous, integration between GPS and indoor positioning can be made.

## Challenge

The problem of Wi-Fi based indoor localization of a device consists in determining the position of client devices with respect to access points. Many techniques exist to accomplish this, and these may be classified into three main types:

- Received signal strength indication (RSSI) fingerprinting
- Angle of arrival (AoA)
- Time of flight (ToF) based techniques.

We have chose the most common and widespread localization technique used for positioning with wireless access points, i.e. measuring the intensity of the received signal (Received signal strength indication or RSSI) and the method of "fingerprinting" via utilizing machine learning algorithm called [Random Forest](https://en.wikipedia.org/wiki/Random_forest).

Unfortunately, Wi-Fi signal strength measurements are extremely noisy, so there is ongoing research focused on making more accurate systems by using statistics to filter out the inaccurate input data.

## Accuracy

Anything around ~10 meters or more should get >99% accuracy.

It is the most robust when you switch locations and train in turn. E.g. first in Spot A, then in Spot B then start again with A. Doing this in spot A, then spot B and then immediately using "predict" will yield spot B as an answer usually. The effect of this temporal overfitting disappears over time. And, in fact, this is only a real concern for the very short distances. Just take a sample after some time in both locations and it should become very robust.

Surprisingly, vertical difference in location is typically even more distinct than horizontal differences.

## Demo

![MINN Demo](/static/demo.gif)

## Usage

```console
root@woot:~/MINN$ python cli.py

usage: cli.py [-h] [--version]
              {predict,predict_proba,crossval,ls,locations,learn,rename,train}
              ...

Uses WiFi signals and machine learning to predict where you are.
Feel free to try out commands, if anything is missing it will print help.

You will want to start with `cli.py learn`

positional arguments:
  {predict,predict_proba,crossval,ls,locations,learn,rename,train}

optional arguments:
  -h, --help            show this help message and exit
  --version, -v         show program's version number and exit
```

## Installation

#### Step 1: (Cloning the Repository)

```
git clone https://github.com/0x48piraj/MINN
```

#### Step 2: (Installing the batteries)
```
cd MINN && pip install -r requirements.txt
```

## Dependencies

- [tqdm](https://github.com/tqdm/tqdm)
- [Scipy](https://github.com/scipy/scipy/)
- [Numpy](https://github.com/numpy/numpy)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)


