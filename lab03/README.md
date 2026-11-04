# Lab 3 — How Machine Learning Learns

## Learning objectives

By the end of this lab, you should be able to:

- Explain how a model converts input features into predictions using adjustable **parameters**.
- Implement a simple linear prediction function using NumPy, without using a ready-made model's `.fit()` method.
- Calculate prediction errors and compare **mean absolute error (MAE)** and **mean squared error (MSE)**.
- Explain that training aims to find parameters that minimize a **loss function**.
- Implement gradient descent and track parameter updates and training loss over time.
- Experiment with **learning rates** and identify slow, stable, and unstable training behavior.
- Compare **training and validation loss** to recognize underfitting, overfitting, and generalization problems.
- Explain how model complexity and the amount of training data can influence performance on unseen observations.

**Focus:** This lab examines *what happens during learning*. In Lab 4, you will apply ready-made classical machine-learning algorithms using scikit-learn.

## Lab materials

```text
lab03/
├── README.md                    # This guide
├── 01-models-and-loss.ipynb    # Predictions, parameters, and loss
├── 02-gradient-descent.ipynb   # Implement a learning algorithm
├── 03-generalization.ipynb    # Training vs. validation performance
└── data/
    ├── linear_rent.csv         # 72 synthetic apartment observations
    └── nonlinear_data.csv     # 90 synthetic observations with a nonlinear relationship
```

The repository root (one directory above `lab03/`) contains the course-level `README.md`, `requirements.txt`, setup scripts, and `00-environment-check.ipynb`.

## Before you begin

Use the local Python environment established during Lab 1. If you need to create or repair it, open a terminal at the **repository root** and run the appropriate script:

**Windows (Command Prompt):**

```bat
setup-windows.bat
```

**Linux:**

```bash
bash setup-linux.sh
```

If the virtual environment already exists and the packages are installed, start JupyterLab directly:

**Windows:**

```powershell
.venv\Scripts\python.exe -m jupyter lab
```

**Linux:**

```bash
.venv/bin/python -m jupyter lab
```

If you encounter import or environment problems, execute `00-environment-check.ipynb` from the repository root. Lab 3 uses **NumPy, Pandas, and Matplotlib**; it does not require PyTorch or Ultralytics.

In JupyterLab, open the `lab03/` folder and begin with `01-models-and-loss.ipynb`. Work through the notebooks in order.

**Important — file paths:** Keep the notebooks inside `lab03/` and the CSV files inside `lab03/data/`. The notebooks load their data using relative paths such as `data/linear_rent.csv`. Each notebook can be restarted and run independently from top to bottom.

## Suggested three-hour schedule

| Activity | Approximate time | What you will do |
|---|---:|---|
| Introduction | 5 min | Review features, targets, predictions, and the purpose of model training |
| **Notebook 01 — Models and Loss Functions** | 50 min | Experiment with a linear model and measure prediction errors |
| **Notebook 02 — Learning with Gradient Descent** | 60 min | Implement parameter updates and examine learning-rate effects |
| **Notebook 03 — Training Behavior and Generalization** | 55 min | Compare training and validation errors across model complexities |
| Wrap-up and discussion | 10 min | Explain what learning means and connect the results to Lab 4 |
| **Total** | **180 min** | **3 hours** |

These are recommended times. Complete the core examples and exercises first; use any additional time to investigate the mini-challenges.

## Notebook 01 — Models and Loss Functions

**File:** `01-models-and-loss.ipynb`  
**Estimated time:** 50 minutes  
**Dataset:** `data/linear_rent.csv`

You will:

- Load a small apartment dataset and identify **floor area** as the input feature and **monthly rent** as the target.
- Implement the linear prediction function `y_pred = w * x + b` using NumPy.
- Change the **weight** and **bias** to observe how predictions change.
- Compute residuals, **MAE**, and **MSE** using NumPy.
- Compare candidate model parameters and plot how the loss changes.
- Understand why choosing parameters on a dataset is different from assessing generalization to new data.

**Mini-challenge:** Use your selected parameters to predict the rent of a new 75 m² apartment. Explain the prediction and what you would need to know to judge its reliability.

**Checkpoint:** You can explain the distinction between a **model**, its **parameters**, a **prediction**, and a **loss function**.

## Notebook 02 — Learning with Gradient Descent

**File:** `02-gradient-descent.ipynb`  
**Estimated time:** 60 minutes  
**Dataset:** `data/linear_rent.csv`

You will:

- Reload the apartment dataset and standardize the input for stable numerical optimization.
- Understand a **gradient** as information about how the loss changes when parameters change.
- Implement a single gradient-descent update for the weight and bias.
- Combine repeated updates into a training loop and record the loss at each iteration.
- Plot the **learning curve** to see whether training is converging.
- Compare small, moderate, and excessively large learning rates.
- Convert the learned relationship back into meaningful apartment-rent predictions.

**Mini-challenge:** Choose a learning rate and number of iterations, train your own model, and predict rent for a 75 m² apartment. Justify your training settings using the loss curve.

**Checkpoint:** You can explain how repeated parameter updates reduce the loss, and why an inappropriate learning rate can make training slow or unstable.

## Notebook 03 — Training Behavior and Generalization

**File:** `03-generalization.ipynb`  
**Estimated time:** 55 minutes  
**Dataset:** `data/nonlinear_data.csv`

You will:

- Load a new synthetic dataset with a **nonlinear** relationship.
- Create a reproducible **training/validation split**.
- Fit polynomial models of different degrees using NumPy's `polyfit()`.
- Visualize models that are too simple, reasonably flexible, or unnecessarily complex.
- Plot and compare **training and validation MSE** as model complexity changes.
- Explore how increasing the number of training observations affects generalization.
- Select a model using validation performance rather than training error alone.

**Mini-challenge:** Compare polynomial degrees 1 through 12 and recommend a model. Support your choice with training and validation losses and a brief explanation of underfitting or overfitting.

**Checkpoint:** You can explain why the model with the lowest training error is not necessarily the best model for unseen data.

## About the datasets

Both datasets are **synthetic**, produced for teaching purposes. They are not observations from a real housing market or a real scientific experiment.

### `linear_rent.csv`

Contains **72 apartment observations** and three columns:

| Column | Meaning |
|---|---|
| `apartment_id` | Identifier for each synthetic apartment |
| `area_m2` | Floor area in square metres (input feature) |
| `monthly_rent_eur` | Monthly rent in euros (prediction target) |

This dataset has a deliberately simple relationship so that you can concentrate on the mathematics and behavior of training. It is used in **Notebooks 01 and 02**.

### `nonlinear_data.csv`

Contains **90 synthetic observations** and two columns:

| Column | Meaning |
|---|---|
| `input_x` | Numerical input feature |
| `target_y` | Numerical target with a nonlinear relationship and noise |

This dataset is used in **Notebook 03** to explore model complexity and generalization.

**Do not modify the supplied CSV files.** Experiment on values and arrays inside the notebooks so that you can always restart with the original data.

## Working with the notebooks

- Read the short explanations, then **run the examples in order**.
- Complete the **Exercise**, **TODO**, and **Mini-challenge** sections yourself.
- Where requested, add a brief explanation in a Markdown cell. A successful plot is not enough unless you understand its meaning.
- When comparing experiments, change **one setting at a time** whenever possible.
- Restart the kernel and run all cells from the top if notebook variables become inconsistent.
- Save your notebooks regularly. On university lab computers, make sure your work is stored in a **persistent location** or copied to your own device.
- You do not need to submit the datasets; keep them next to the notebooks so the relative paths work.

## What to have at the end

Your completed work should include:

1. **`01-models-and-loss.ipynb`:** predictions from your linear model, calculated losses, parameter comparisons, and the mini-challenge.
2. **`02-gradient-descent.ipynb`:** a gradient-descent training loop, learning-rate experiments, training-loss plots, and an explanation of the resulting behavior.
3. **`03-generalization.ipynb`:** comparisons of polynomial models, training/validation error plots, and a justified model recommendation.

Follow your instructor's directions for any submission. The most important outcome is that you can **explain why and how a model learns**, not simply reproduce code that runs.

## Troubleshooting

| Problem | What to check |
|---|---|
| `FileNotFoundError` for a CSV | Open the notebook from `lab03/` and keep both files in `lab03/data/`. |
| `ModuleNotFoundError` for NumPy, Pandas, or Matplotlib | Start JupyterLab using `.venv` and verify packages with the course environment-check notebook. |
| `NameError` for a variable | Run earlier code cells in the current notebook, or restart the kernel and run from the beginning. |
| Loss increases or becomes `inf` / `nan` | In Notebook 02, try a smaller learning rate and check input scaling. |
| Unexpectedly poor predictions | Inspect the input units, weight, bias, and whether you are using the standardized or original feature values. |
| Polynomial fit warning or erratic curve | In Notebook 03, try a lower polynomial degree; high-degree polynomial fits may be numerically unstable. |
| Plot does not appear | Ensure the code cell executed successfully and that Matplotlib is installed in the active kernel. |
| Notebook changes disappear after logging out | Save to persistent storage or copy completed notebooks to your own device. |

Consult the course-level `README.md` for additional setup instructions.

## Looking ahead: Lab 4

Lab 3 showed how models make predictions, how a loss function measures error, how gradient descent improves parameters, and why validation is important.

In **Lab 4 — Classical Machine Learning**, you will use scikit-learn to apply these ideas to practical regression and classification tasks. You will train a model to predict apartment rents, classify handwritten digits, compare algorithms, and investigate model overfitting. The `.fit()` method automates many of the learning steps you examined manually in this lab.
