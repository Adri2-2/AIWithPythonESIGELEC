# Lab 4 — Classical Machine Learning: Regression and Classification

## Learning objectives

By the end of this lab, you should be able to:

- Apply **scikit-learn** to train models for regression and classification problems.
- Explain the roles of **features**, **targets**, `.fit()`, and `.predict()`.
- Combine preprocessing and regression into a reproducible **Pipeline**.
- Evaluate regression predictions using **MAE**, **RMSE**, and **R²**, and compare against a simple baseline.
- Train **k-nearest neighbors**, **logistic regression**, and **decision tree** classifiers.
- Evaluate classification with **accuracy**, a **confusion matrix**, and per-class **precision, recall, and F1-score**.
- Compare training and validation performance, recognize signs of **underfitting** or **overfitting**, and choose hyperparameters using validation data.
- Explain why a final test set should not be used to tune a model.

**Focus:** Lab 3 explored *how learning works* by implementing models, losses, and gradient descent. Lab 4 uses ready-made classical machine-learning algorithms to solve practical supervised-learning tasks. Different algorithms do not necessarily learn in the same way.

## Lab materials

```text
lab04/
├── README.md                     # This guide
├── 01-regression.ipynb           # Predict apartment rent
├── 02-classification.ipynb       # Classify handwritten digits
├── 03-model-comparison.ipynb     # Compare complexity and select models
└── data/
    ├── apartments_corrupted.csv  # 502 original synthetic apartment records
    └── digits.csv                # 1,797 handwritten digits
```

The repository root (one directory above `lab04/`) contains the course-level `README.md`, `requirements.txt`, setup scripts, and `00-environment-check.ipynb`.

## Before you begin

Use the local Python environment established in Lab 1. If you need to set it up or repair it, open a terminal in the **repository root** and run:

**Windows (Command Prompt):**

```bat
setup-windows.bat
```

**Linux:**

```bash
bash setup-linux.sh
```

If the environment already exists, launch JupyterLab directly from the repository root:

**Windows:**

```powershell
.venv\Scripts\python.exe -m jupyter lab
```

**Linux:**

```bash
.venv/bin/python -m jupyter lab
```

This laboratory uses **NumPy, Pandas, Matplotlib, and scikit-learn**. It does not require PyTorch or Ultralytics. If imports fail, run `00-environment-check.ipynb` from the repository root.

In JupyterLab, open the `lab04/` folder, then work through the three notebooks in order.

**Important — file paths:** Keep the notebooks inside `lab04/` and both CSVs inside `lab04/data/`. The notebooks read files through relative paths such as `data/digits.csv`. Run each notebook with `lab04/` as its working directory. Each notebook can be restarted and executed independently from top to bottom.

## Suggested three-hour schedule

| Activity | Approximate time | What you will do |
|---|---:|---|
| Introduction | 5 min | Connect Lab 3's learning concepts to scikit-learn's `.fit()` and `.predict()` |
| **Notebook 01 — Regression** | 60 min | Train and evaluate a model that predicts apartment rent |
| **Notebook 02 — Classification** | 60 min | Classify handwritten digits and interpret errors |
| **Notebook 03 — Model Comparison** | 50 min | Explore hyperparameters, overfitting, and model selection |
| Wrap-up and discussion | 5 min | Compare tasks and discuss generalization |
| **Total** | **180 min** | **3 hours** |

Prioritize the core exercises before attempting optional challenges. Save work regularly.

## Notebook 01 — Regression: Predicting Apartment Rent

**File:** `01-regression.ipynb`  
**Estimated time:** 60 minutes  
**Dataset:** `data/apartments_corrupted.csv`

You will:

- Load an apartment dataset and apply predefined, rule-based cleaning checks.
- Separate input features (such as area, rooms, and district) from the target **monthly rent**.
- Create training and test subsets using a reproducible split.
- Combine imputation, scaling, categorical encoding, and `LinearRegression` in a **Pipeline**.
- Train with `.fit()` and produce estimates using `.predict()`.
- Compare regression against a **median-prediction baseline**.
- Interpret **MAE (euros)**, **RMSE (euros)**, and **R²**, and inspect actual-vs-predicted and residual plots.
- Predict rent for a new apartment, including a previously unseen category.

**Mini-challenge:** Define a new apartment, predict its rent, and explain how changing its characteristics affects the model's prediction.

**Checkpoint:** You can explain how the preprocessing and model are combined, why the baseline matters, and what prediction errors mean in practical units.

**Connect to Lab 3:** A model still learns parameters from examples, but scikit-learn handles the fitting procedure; not every estimator uses the gradient-descent algorithm you coded previously.

## Notebook 02 — Classification: Recognizing Handwritten Digits

**File:** `02-classification.ipynb`  
**Estimated time:** 60 minutes  
**Dataset:** `data/digits.csv`

You will:

- Load pixel features from a CSV and reconstruct **8 × 8 grayscale digit images**.
- Separate the 64 input pixels from the target digit label (0–9).
- Create reproducible, **stratified training, validation and test** splits, preserving the test set for Notebook 03.
- Train a **k-nearest neighbors** classifier and compare its predictions with a majority-class baseline.
- Train **logistic regression** and a **decision tree** for the same task.
- Compare predictions using **validation accuracy**, **precision**, **recall**, and **F1-score**.
- Display a **validation confusion matrix** and investigate incorrectly classified digits.

**Mini-challenge:** Select a digit image, compare predictions from the three classifiers, and explain any disagreements or mistakes.

**Checkpoint:** You can explain the difference between regression and classification, and identify common classification errors rather than relying on accuracy alone.

## Notebook 03 — Model Comparison and Overfitting

**File:** `03-model-comparison.ipynb`  
**Estimated time:** 50 minutes  
**Dataset:** `data/digits.csv`

You will:

- Work with separate **training**, **validation**, and **test** subsets.
- Vary the number of neighbors (**k**) in k-NN and plot training versus validation accuracy.
- Vary decision-tree **maximum depth** and observe changes in model complexity.
- Recognize **underfitting**, **overfitting**, and differences between training and validation performance.
- Compare candidate models using validation results.
- Evaluate the chosen model on held-out test examples, then inspect its confusion matrix.

**Mini-challenge:** Find a misclassified digit in the final evaluation, display the image, and propose a possible reason for the error.

**Checkpoint:** You can defend a model choice using validation evidence and explain why repeatedly checking test-set scores while tuning models is misleading.

**Note on experimental discipline:** Notebooks 02 and 03 use the **same reproducible, stratified 64% training / 16% validation / 20% test split** (`random_state=42`). Notebook 02 trains classifiers and explores predictions **only on the training and validation subsets**. Notebook 03 uses validation data to select hyperparameters and then evaluates the chosen model **once on the reserved test set**. Avoid looking at test examples or tuning models after this final assessment.

## About the datasets

### `apartments_corrupted.csv`

This is the synthetic apartment dataset reused from Lab 2, containing **502 original records and nine columns**. It includes missing values, inconsistent categories, invalid measurements, and duplicate records. The regression notebook applies fixed cleaning rules before model training; the number of usable observations is therefore lower than 502.

| Column | Meaning |
|---|---|
| `apartment_id` | Apartment identifier (not a predictive feature) |
| `area_m2` | Apartment area in square metres |
| `rooms` | Number of rooms |
| `building_age_years` | Building age in years |
| `distance_to_center_km` | Distance to city centre in kilometres |
| `district` | District category |
| `balcony` | Whether a balcony is available |
| `energy_rating` | Energy-efficiency category |
| `monthly_rent_eur` | Monthly rent in euros (**regression target**) |

### `digits.csv`

Contains **1,797 handwritten digit samples**, each stored as 64 pixel features (`pixel_0` through `pixel_63`) and one `target` label. Each set of 64 pixels can be reshaped into an **8 × 8 image**. The label is an integer from **0 through 9**. The pixel values in this teaching dataset range from **0 to 16**.

The two datasets support different supervised-learning tasks: apartment rent is a **continuous regression target**, while the digit label is a **categorical classification target**.

**Do not alter the supplied CSV files.** Make experimental changes inside your notebooks so you can restart from the original data.

## Working with notebooks and exercises

- Read each explanation and execute example cells in order.
- Complete sections marked **Exercise**, **TODO**, or **Mini-challenge** independently.
- Add short Markdown interpretations where requested; a number or chart alone is not a sufficient conclusion.
- When comparing model settings, change one setting at a time whenever possible.
- Remember that the role of an input feature differs from the role of a target label.
- Restart the kernel and run cells from the top if earlier variables were changed or lost.
- Save completed notebooks to persistent storage, particularly if university computers reset between sessions.

## What to have at the end

Your completed work should contain:

1. **`01-regression.ipynb`:** a preprocessing-and-regression pipeline, comparisons with a baseline, evaluation metrics, plots, and a new-apartment prediction.
2. **`02-classification.ipynb`:** at least three classification approaches, a comparison of performance, a confusion matrix, and discussion of classification errors.
3. **`03-model-comparison.ipynb`:** training/validation accuracy curves, an explained model choice, and a final test evaluation.

Follow your instructor's directions for any submission. **Your explanations of model behavior and errors are as important as executable code.**

## Troubleshooting

| Problem | What to check |
|---|---|
| `FileNotFoundError` | Keep the notebooks in `lab04/` and CSVs in `lab04/data/`; run with `lab04/` as working directory. |
| `ModuleNotFoundError` | Launch JupyterLab using the course `.venv` and run the environment check. |
| `NameError` | Run earlier cells in order, or restart the kernel and run all cells. |
| Unexpected categorical-imputer error | Ensure missing categorical entries are represented consistently; use the cleaning function provided in Notebook 01. |
| Unexpectedly poor model accuracy | Check features/labels, the split, preprocessing, and model parameters before changing multiple things. |
| Confusion matrix looks inconsistent | Confirm the true labels and predictions come from the same data partition and the same model. |
| Long-running model fitting | Let the current fit complete; avoid unnecessary repetitions, especially when changing many parameters. |
| Work disappears after logging out | Save notebooks to a persistent location or copy them to your own device. |

Consult the course-level `README.md` for additional environment setup help.

## Looking ahead

The next part of the course introduces neural networks, deep learning, and computer vision. The classification experience from handwritten digits prepares you to work with image-related learning tasks, while the data preparation and evaluation practices remain important for the webcam-based group projects.
