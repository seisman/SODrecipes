# SOD Recipes

[SOD](http://www.seis.sc.edu/sod/)，全称是 Standing Order for Data，是一个可以实现自动筛选、下载、预处理地震数据的工具。

SOD 的配置文件称为 recipe，本项目收集了一些常用的 recipe 片段。

- [英文官方教程](http://www.seis.sc.edu/sod/documentation/tutorials/index.html)
- [中文入门教程](https://blog.seisman.info/sod-notes/)

## GenRecipe.py

`GenRecipe.py` 是一个功能简单的Python脚本，用于将多个Arm的recipe片段合并到一个recipe中。

**用法:**
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

**示例:**
```
$ python GenRecipe.py -e eventArm/origin-mag-depth.xml -n networkArm/network.xml -w waveformArm/sacWriter.xml > myrecipe.xml
```

## SOD Arms

### eventArm

- [origin-magnitude-depth-boxarea.xml](eventArm/origin-magnitude-depth-boxarea.xml): 基于发震时刻、位置、震级和深度筛选地震事件，并将结果保存到CSV文件中
- [complexEvent.xml](eventArm/complexEvent.xml): 利用 `originOR` 和 `originAND` 组合筛选出复杂规则下的地震目录
- [custom-events-from-csv.xml](eventArm/custom-events-from-csv.xml): 从指定的 [CSV文件](eventArm/customEvents.csv) 中读入事件信息
- [custom-events.xml](eventArm/custom-events.xml): 直接在 recipe 中指定事件信息
- [continuous-waveform.xml](eventArm/continuous-waveform.xml): 生成伪事件用于获取连续波形数据

### networkArm

- [network.xml](networkArm/network.xml): 选择一个台网
- [networkOR.xml](networkArm/networkOR.xml): 选择多个台网
- [stationOR.xml](networkArm/stationOR.xml): 显式指定多个台站

### waveformArm

- [breqfast.xml](waveformArm/breqfast.xml): 生成 BREQ_FAST 文件
- [sacWriter.xml](waveformArm/sacWriter.xml): 以 SAC 格式写入到磁盘并作数据预处理、去仪器响应、标记到时
