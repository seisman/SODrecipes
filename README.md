# SOD recipes

[SOD](http://www.seis.sc.edu/sod/), Standing Order for Data, is a framework to define rules to select seismic events, stations and data.

## GenRecipe.py

`GenRecipe.py` is a Python script to copy ready-to-use arms into one recipe.

**Usage:**
```
$ python GenRecipe.py -h
usage: GenRecipe.py [-h] [-e EVENTARM] [-n NETWORKARM] [-w WAVEFORMARM]

Paste event, network and waveform arms into one xml.

optional arguments:
  -h, --help      show this help message and exit
  -e EVENTARM     specify eventArm
  -n NETWORKARM   specify networkArm
  -w WAVEFORMARM  specify waveformArm
```

**Example:**
```
$ python GenRecipe.py -e eventArm/origin-mag-depth.xml -n networkArm/network.xml -w waveformArm/sacWriter.xml > myrecipe.xml
```

## SOD Arms

### eventArm

- [origin-mag-depth.xml](eventArm/origin-mag-depth.xml): Select events based on origin time, magnitude and depth, and save the selected events to csv file

### networkArm

- [network.xml](networkArm/network.xml): Select one network only
- [networkOR.xml](networkArm/networkOR.xml): Select multiple networks
- [stationOR.xml](networkArm/stationOR.xml): Select multiple stations

### waveformArm

- [breqfast.xml](waveformArm/breqfast.xml): generate breqfast files
- [sacWriter.xml](waveformArm/sacWriter.xml): write to SAC files
