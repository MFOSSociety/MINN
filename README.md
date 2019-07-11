# Inn

Wi-Fi indoor positioning system for Manipal University Jaipur.

Works without Internet/GPS/Anything!

## Why this Project (?)

Global navigation satellite systems (GPS or GNSS) are generally not suitable to establish indoor locations, since microwaves will be attenuated and scattered by roofs, walls and other objects. However, in order to make positioning signals ubiquitous, integration between GPS and indoor positioning can be made.

# Challenge

The problem of Wi-Fi based indoor localization of a device consists in determining the position of client devices with respect to access points. Many techniques exist to accomplish this, and these may be classified into three main types:

- Received signal strength indication (RSSI), fingerprinting
- Angle of arrival (AoA)
- Time of flight (ToF) based techniques.

We have chose the most common and widespread localization technique used for positioning with wireless access points, i.e. measuring the intensity of the received signal (Received signal strength indication or RSSI) and the method of "fingerprinting" via utilizing machine learning algorithm called [Random Forest](https://en.wikipedia.org/wiki/Random_forest).

Unfortunately, Wi-Fi signal strength measurements are extremely noisy, so there is ongoing research focused on making more accurate systems by using statistics to filter out the inaccurate input data.

