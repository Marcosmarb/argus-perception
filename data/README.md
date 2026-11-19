# Data

Datasets are **not** committed to this repository.

This project uses the **VisDrone2019-MOT** dataset (aerial video sequences with
multi-object tracking ground truth).

- Official site: https://github.com/VisDrone/VisDrone-Dataset
- Download one sequence from the MOT validation split and place it here, e.g.:

```
data/
└── VisDrone2019-MOT-val/
    ├── sequences/<sequence_name>/0000001.jpg ...
    └── annotations/<sequence_name>.txt
```

Exact download and setup steps will be documented once the `video_publisher`
node is implemented.
