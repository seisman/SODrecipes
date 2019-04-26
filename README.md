# SOD Recipes

[SOD](http://www.seis.sc.edu/sod/) (Standing Order for Data), is a program
that automates tedious data selection, downloading, and routine processing tasks
in seismology. Files that configure SOD's operation are called recipes.

If you're new to SOD, you can refer to the [official tutorial](http://www.seis.sc.edu/sod/documentation/tutorials/index.html)
or [a Chinese tutorial](https://blog.seisman.info/sod-notes/) written by me.

This project collects some common-used recipes.

## SOD Arms

### eventArm

- [origin-magnitude-depth-boxarea.xml](eventArm/origin-magnitude-depth-boxarea.xml): Select events based on origin time, location, magnitude and depth
- [complexEvent.xml](eventArm/complexEvent.xml): Select events based on complex rules
- [custom-events-from-csv.xml](eventArm/custom-events-from-csv.xml): Read events information from [a CSV file](eventArm/customEvents.csv)
- [custom-events.xml](eventArm/custom-events.xml): Custom events information
- [continuous-waveform.xml](eventArm/continuous-waveform.xml): Fake events for continuous waveform data

### networkArm

- [network.xml](networkArm/network.xml): Select one network
- [networkOR.xml](networkArm/networkOR.xml): Select multiple networks
- [stationOR.xml](networkArm/stationOR.xml): Select multiple stations

### waveformArm

- [breqfast.xml](waveformArm/breqfast.xml): Generate requests which can be further used in BREQ_FAST
- [sacWriter.xml](waveformArm/sacWriter.xml): Request data, basic data processing and save data in SAC format

## Full Recipes
