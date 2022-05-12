# RPLidar-Processing
Python function for implementing multi threading in accessing RPLidar values.

## Prerequisites

The function requires the [Rplidar](https://github.com/SkoltechRobotics/rplidar) libary to work.
The serial port for the RPLidar must be changed in the Class at the following line-

```
self.lidar = RPLidar('/dev/ttyUSB0')
```

The class can be imported as-

```
from LidarClass import Lidar_Class
```

Then the class object needs to be initialized.

```
lidar = Lidar_Class().start()
```

The values can be read using the following line-

```
values=lidar.read()
```

The code has been tested on RPLidar A1 with the Rapsberry pi model 3b and windows 10.
