# Artificial Intelligence with Python

Welcome to **Artificial Intelligence with Python**, a practice-oriented course. You will learn how to work with data in Python and build, evaluate, and explain machine-learning models.

**Prerequisites:** Prior programming experience (for example, Java). No previous experience with Python, artificial intelligence, or machine learning is required.

**Course format:** Seven teaching units, each consisting of a **1-hour lecture** followed by a **3-hour laboratory** (7 hours of lectures and 21 hours of labs). The later labs include student-defined projects and presentations.

## What you will learn

- Use Python, JupyterLab, NumPy, Pandas, and Matplotlib for data analysis.
- Load datasets from CSV files; inspect, clean, and visualize data.
- Prepare features and split data appropriately for machine learning.
- Train classification and regression models with scikit-learn.
- Assess models using appropriate metrics and avoid common pitfalls such as data leakage and overfitting.
- Object detection using deep neural networks with PyTorch and Ultralytics.
- Apply the complete workflow to a small project and present your results.

## Course materials

The repository is organized by laboratory. The initial layout is:

```text
AIWithPython/
├── README.md
├── requirements.txt
├── setup-windows.bat
├── setup-linux.sh
├── LectureSlides.pdf
├── 00-environment-check.ipynb
├── lab01/
├── lab02/
├── lab03/
├── lab04/
├── lab05/
```

## Getting started

You will work **locally**, using JupyterLab and a Python virtual environment (`.venv`). You do not need to install Python packages system-wide or have administrator access to install the course packages, provided Python and its virtual environment support are already available.

### 1. Obtain the course repository

If Git is installed, open a terminal and clone the repository:

```bash
git clone https://github.com/WYTan-THMA/AIWithPythonESIGELEC.git
cd AIWithPython
```

Clone the git repository locally. If Git is not installed, download the repository as a ZIP archive, extract it to a **writable folder** (for example, your home directory), and open a terminal in the extracted folder.

All commands below should be run from the **repository root** (the folder containing `requirements.txt`).

### 2. Check Python

The course materials target **Python 3.11 or newer**. A supported version of Python 3 and working `venv` support are needed.

**Windows (PowerShell or Command Prompt):**

```powershell
python --version
```

If `python` is not found, try `py -3 --version` and ask the instructor for assistance if the setup script cannot find Python.

**Linux:**

```bash
python3 --version
```

On Ubuntu/Debian, if creating a virtual environment fails due to missing `venv` support, you may need to install `python3-venv` (administrator privileges are required for that operating-system installation):

```bash
sudo apt update
sudo apt install python3-venv
```

### 3. Set up and launch JupyterLab

Choose the instructions for your operating system. The scripts create `.venv` if necessary, install the packages listed in `requirements.txt`, and start JupyterLab.

#### Windows

In **Command Prompt** or **PowerShell**, from the repository root:

```bat
setup-windows.bat
```

The batch file is intended for a Windows computer with Python available as the `python` command. If you run into an error, show the complete terminal output to the instructor.

#### Linux

From a terminal in the repository root:

```bash
bash setup-linux.sh
```

Alternatively, you can make it executable and run it directly:

```bash
chmod +x setup-linux.sh
./setup-linux.sh
```

**Note:** The first run may take longer because packages are downloaded. Internet access to the Python package index is required unless packages have been made available offline.

### 4. Verify your environment

When JupyterLab opens in your browser:

1. Open **`00-environment-check.ipynb`** in the repository root.
2. Select the Python kernel belonging to `.venv` if prompted.
3. Use **Run → Run All Cells** (or run each cell in order).
4. Check the final summary. The package and functional tests should report **PASS**.

The notebook tests the Python version, imports, NumPy operations, Pandas and CSV handling, plotting, and a simple scikit-learn model. It does **not** install packages.

If JupyterLab starts but the notebook reports missing packages, check which Python interpreter the notebook is using. Its path should normally contain `.venv`.

### 5. Work on the lab exercises

Open the notebooks for the current lab inside JupyterLab. Execute cells from top to bottom and complete the exercises marked `TODO`. Include your own explanations and observations, not just code.

Keep a copy of your work in a location that survives logging out of the university computers. Save your notebook regularly.

## Starting JupyterLab again

It is fine to run the same setup script again: the existing virtual environment will be reused, although required packages will still be checked.

For a faster start when the environment is already set up, run JupyterLab directly from the repository root:

**Windows:**

```powershell
.venv\Scripts\python.exe -m jupyter lab
```

**Linux:**

```bash
.venv/bin/python -m jupyter lab
```

You do not need to activate the virtual environment when invoking its Python interpreter by its full relative path.

## Troubleshooting

| Problem | What to try |
|---|---|
| `python` or `python3` is not found | Check Python installation and the system PATH; on Windows try `py -3 --version`. |
| Virtual environment creation fails | Check that `venv` is installed and that your chosen directory is writable. |
| A Python package fails to install | Check the internet connection and copy the full error message for the instructor. |
| Notebook reports `ModuleNotFoundError` | Start JupyterLab using `.venv`'s Python and choose the corresponding kernel. |
| JupyterLab doesn't open in a browser | Look for a local URL containing a token in the terminal and open it in your browser. |
| Cannot write files | Move the repository to a folder where your user account has write permissions. |
| Changes disappear after logout | Store your work on persistent storage or back it up before leaving. |

To reinstall course dependencies into an existing `.venv`, run:

**Windows:**

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Linux:**

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Later course sessions

Some optional advanced exercises may require additional packages, cameras, or compatible hardware. Any extra setup for deep learning or computer vision will be communicated with those labs; it is not part of the initial environment setup.

---

**Instructor:** Prof. Dr.-Ing. Wei Yap Tan  
**Course:** Artificial Intelligence with Python  
