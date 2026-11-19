# Argus Perception

> Work in progress.

ROS 2 perception pipeline that detects and tracks targets in aerial drone video
([VisDrone](https://github.com/VisDrone/VisDrone-Dataset)).

## Goal

```
video_publisher ──► detector (YOLO) ──► tracker (ByteTrack) ──► overlay ──► rqt_image_view / RViz2
   sensor_msgs/Image      vision_msgs/Detection2DArray          annotated image
```

1. Publish a VisDrone sequence as if it were the drone camera.
2. Detect objects with YOLO and publish standard `vision_msgs/Detection2DArray` messages.
3. Track targets with ByteTrack so each one keeps a stable ID.
4. Visualize boxes and IDs.
5. Measure FPS, end-to-end latency and, if time allows, tracking metrics (MOTA/HOTA).
6. Launch everything with a single command.

## Status

| Component | Status |
|---|---|
| `video_publisher` | Planned |
| `detector` | Planned |
| `tracker` | Planned |
| `overlay` + launch | Planned |
| Benchmarks | Planned |

## Results

No results yet. All numbers in this section will come from real measurements
on the hardware listed below.

## Requirements

- Ubuntu 24.04 (tested on WSL2)
- ROS 2 Jazzy
- Python 3.12

## Installation

Clone into the `src/` folder of a colcon workspace:

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone https://github.com/Marcosmarb/argus-perception.git
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## Data

See [data/README.md](data/README.md).

## License

[Apache 2.0](LICENSE)
