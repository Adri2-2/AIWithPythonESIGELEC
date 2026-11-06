# Lab 5 — Introduction to Deep Learning and Computer Vision

## Learning objectives

By the end of this lab, you should be able to:

- Construct and train a small neural network in PyTorch using a familiar classification dataset.
- Explain forward passes, loss functions, backpropagation, optimizers, and validation accuracy.
- Run object detection using a pretrained Ultralytics YOLO model on a photograph and video frame.
- Read bounding-box coordinates, class labels, and confidence scores.
- Use OpenCV with a local webcam or supplied fallback video.
- Capture a small collection of images and annotate bounding boxes using **CVAT Online**.
- Recognize the structure of a YOLO Detection dataset and explain when YOLO Pose annotation is appropriate.

## Folder structure

```text
lab05/
├── README.md
├── requirements-lab05.txt
├── .gitignore
├── 00-environment-check.ipynb
├── 01-pytorch-neural-network.ipynb
├── 02-yolo-object-detection.ipynb
├── 03-webcam-and-dataset.ipynb
├── data/
│   ├── digits.csv
│   ├── sample.jpg
│   └── sample_video.mp4
├── scripts/
│   ├── webcam_detection.py
│   ├── webcam_capture.py
│   └── train_custom_yolo.py     # OPTIONAL: project template
└── examples/
    └── yolo_dataset/
        ├── data.yaml
        ├── images/{train,val}/
        └── labels/{train,val}/
```

## Before you begin: install the additional packages

Use the **same course virtual environment** (`.venv`) from Labs 1–4. Open a terminal at the **repository root** and run:

**Windows (Command Prompt or PowerShell)**

```bat
.venv\Scripts\python.exe -m pip install -r lab05/requirements-lab05.txt
.venv\Scripts\python.exe -m jupyter lab
```

**Linux**

```bash
.venv/bin/python -m pip install -r lab05/requirements-lab05.txt
.venv/bin/python -m jupyter lab
```

PyTorch downloads can be large. So the installation might take some time.

In JupyterLab, open `lab05/` and run `00-environment-check.ipynb` first. The notebooks load local files with paths relative to `lab05/` (e.g. `data/sample.jpg`).

**First YOLO use** may download `yolo11n.pt` automatically. The sample image and sample video are already included and do not need internet access, but inference requires the model weights.

## Notebook 01 — Your First Neural Network with PyTorch (35 min)

**File:** `01-pytorch-neural-network.ipynb`  
**Dataset:** `data/digits.csv` (1,797 examples, 64 features, 10 classes)

- Convert Pandas/NumPy arrays to tensors.
- Create `Linear → ReLU → Linear` network.
- Use `CrossEntropyLoss` and Adam to update network weights.
- Plot training and validation loss/accuracy and visualize prediction errors.
- **Mini-challenge:** Change the learning rate or hidden layer width, train again, and interpret results.

**Checkpoint:** Understand how neural networks learn and how that differs from directly calling scikit-learn's `.fit()`.

## Notebook 02 — Object Detection with Ultralytics YOLO (30 min)

**File:** `02-yolo-object-detection.ipynb`  
**Input:** `data/sample.jpg`

- Compare classification and object detection.
- Load pretrained `yolo11n.pt` and run inference on the sample image.
- Display bounding boxes and inspect class names, confidence, and pixel coordinates.
- Change the confidence threshold and analyze false positives or missed objects.
- **Mini-challenge:** Count instances of a selected class or test another permitted image.

**Checkpoint:** Explain exactly what a pretrained detector produces; detection is not the same as training a custom model.

## Notebook 03 — Webcam, CVAT Annotation, and YOLO Datasets (65 min)

**File:** `03-webcam-and-dataset.ipynb`  
**Input:** `data/sample_video.mp4`, optional webcam, and a tiny synthetic example dataset.

- Use OpenCV to inspect video frames and YOLO to annotate a frame.
- Run `scripts/webcam_detection.py` for live webcam detection (or fallback to the video).
- Capture 8–12 local photographs using `scripts/webcam_capture.py`.
- Create a **standalone CVAT task** without assigning it to a project, upload images, draw boxes, and export YOLO Detection annotations.
- Inspect `.txt` annotation rows and `data.yaml`; understand normalized bounding boxes.
- Briefly discuss Pose keypoint annotation and when it would be needed.

### Running the webcam scripts

From the **repository root**:

| Action | Windows | Linux |
|---|---|---|
| Detection | `.venv\Scripts\python.exe lab05/scripts/webcam_detection.py --source 0` | `.venv/bin/python lab05/scripts/webcam_detection.py --source 0` |
| Capture photos | `.venv\Scripts\python.exe lab05/scripts/webcam_capture.py --source 0 --output lab05/captures` | `.venv/bin/python lab05/scripts/webcam_capture.py --source 0 --output lab05/captures` |
| Detection without a webcam | Add `--source lab05/data/sample_video.mp4` | Add `--source lab05/data/sample_video.mp4` |

Press **Q** to end a script and **SPACE** in the capture window to save an image. If the desktop preview cannot open, use the offline video with the Notebook 03 frame exercise; webcam access is not required to finish all core exercises.

### Guided CVAT task (no project required)

1. Sign in to [CVAT Online](https://app.cvat.ai/). You may use your github or google account.
2. Open **Tasks → Create new task** and name it `Lab5-Object-Detection`.
3. **Leave the Project field empty**, preserving the project allowance for the students' real group project.
4. Add labels appropriate for your photos (e.g. `cup`, `bottle`), draw rectangles, and save annotations.
5. Export **Ultralytics YOLO Detection** annotations. Keep original images locally, because free accounts may not provide image export.
6. Verify label class indices and image filenames in the exported archive. Annotation task limits and feature availability can change.

CVAT documentation: [Creating tasks](https://docs.cvat.ai/docs/workspace/tasks-page/) and [YOLO formats](https://docs.cvat.ai/docs/manual/advanced/formats/format-yolo-ultralytics/).

### YOLO Detection versus Pose

For object detection, labels contain `class x_center y_center width height` in normalized coordinates. For Pose, annotations contain additional **ordered keypoints**, a consistent skeleton specification, and different training requirements. The guided exercise uses Detection; custom skeleton annotation is an optional project path.

**Note:** `examples/yolo_dataset/` is a tiny made-up red-square/blue-circle dataset to explain file structure and bbox coordinates. It is **not** a benchmark and should not be used to infer real detector accuracy.

## What to have at the end

- A completed PyTorch notebook with learning curves and a brief interpretation.
- A YOLO inference notebook with boxes, detected labels and confidence-threshold observations.
- A live demo using a webcam **or** a successful annotated frame from the fallback video.
- A small CVAT standalone task with exported labels (or a reviewed instructor-provided export if account access is unavailable).
- A short team-project idea with proposed labels, collection plan, train/validation split, and live demonstration.

## Troubleshooting

| Problem | What to try |
|---|---|
| Large or failed PyTorch install | Use a supported Python version, stable network connection, and official PyTorch installer selector; use CPU mode unless GPU hardware is verified |
| `ModuleNotFoundError` | Use the `.venv` Python to install `requirements-lab05.txt` and start JupyterLab |
| YOLO weights cannot download | Ask the instructor for a local copy of `yolo11n.pt`; do not assume an internet connection |
| Camera index `0` fails | Try `--source 1`; close other applications using the camera; check device permissions |
| No webcam or no GUI window | Work with `data/sample_video.mp4` inside Jupyter; the continuous GUI script requires a desktop |
| YOLO detects nothing | Try another image, lower threshold, or check whether the object belongs to pretrained classes |
| CVAT export lacks images | Keep your original webcam images and pair them with exported `.txt` labels |
| `FileNotFoundError` for `data/...` | Open and run notebooks within `lab05/` rather than from another directory |
| Exported box seems misplaced | Check label indices, normalization, and pixel coordinates and match names exactly |

## Looking ahead: student projects

You will build a team of **three** and work on a ML-project. You will select a webcam-based idea, collect and label your own images, train/fine-tune an appropriate model, and demonstrate it on a **live camera stream**.

The project will be evaluated based on its completeness, appropriate data handling, working code, and quality of the final presentation.

An optional template for custom training is included at `scripts/train_custom_yolo.py`. **Do not run it on the tiny toy dataset as if it were a realistic project training exercise.**

## References and data credit

- [PyTorch local installation](https://pytorch.org/get-started/locally/)
- [Ultralytics YOLO inference](https://docs.ultralytics.com/modes/predict/)
- [CVAT tasks](https://docs.cvat.ai/docs/workspace/tasks-page/)
- [CVAT Ultralytics formats](https://docs.cvat.ai/docs/manual/advanced/formats/format-yolo-ultralytics/)
- `data/digits.csv`: scikit-learn Digits dataset, already used in Lab 4.
- `data/sample.jpg`: coffee photograph from the scikit-image example data; `sample_video.mp4` is a synthetic pan over the same still image. Credit: scikit-image sample data contributors.
- `examples/yolo_dataset/`: original generated toy shapes and sample bounding-box labels for format instruction only.
