# Lab 2 — Data Preprocessing for Machine Learning

## Learning objectives

By the end of this lab, you should be able to:

- Assess a dataset for missing values, invalid measurements, duplicates, inconsistent categories, and unusual observations.
- Distinguish data-quality problems from legitimate outliers, and explain the reasoning behind cleaning decisions.
- Identify input **features** (`X`), the prediction **target** (`y`), and identifiers that should not be used as predictive features.
- Explain and demonstrate **imputation**, **one-hot encoding**, **standardization**, and **min–max scaling**.
- Split observations into training and test sets and describe **data leakage**.
- Build a reproducible preprocessing workflow with scikit-learn's `Pipeline` and `ColumnTransformer`.
- Apply a fitted preprocessing workflow to previously unseen observations.

**No prediction model is trained in Lab 2.** The goal is to prepare data correctly before learning regression models in Lab 3.

## Lab materials

```text
lab02/
├── README.md                         # This guide
├── 01-data-cleaning.ipynb            # Audit data quality and cleaning rules
├── 02-feature-preprocessing.ipynb    # Imputation, encoding, and scaling
├── 03-preprocessing-pipelines.ipynb  # Train/test split and pipelines
└── data/
    └── apartments_corrupted.csv     # Synthetic dataset with quality problems
```

The repository's **root directory**, one level above `lab02/`, contains `requirements.txt`, the operating-system setup scripts, and `00-environment-check.ipynb`.

## Before you begin

1. Use the same local Python/Jupyter environment as in Lab 1. If needed, open a terminal at the **repository root** and run the setup script:

   **Windows (Command Prompt):**

   ```bat
   setup-windows.bat
   ```

   **Linux:**

   ```bash
   bash setup-linux.sh
   ```

2. If the virtual environment already exists and the packages are installed, you can simply start JupyterLab from the repository root:

   **Windows:**

   ```powershell
   .venv\Scripts\python.exe -m jupyter lab
   ```

   **Linux:**

   ```bash
   .venv/bin/python -m jupyter lab
   ```

3. If you are unsure about your environment, run `00-environment-check.ipynb` from the repository root.
4. In JupyterLab's file browser, open `lab02/` and start with `01-data-cleaning.ipynb`. Continue with notebooks 02 and 03 in order.

**Important — relative data paths:** All three notebooks read `data/apartments_corrupted.csv` relative to the `lab02/` directory. Keep the notebooks and their `data/` folder together. **You do not need to complete Notebook 01 to initialize variables in Notebook 02:** each notebook reloads the original dataset and runs independently from the top.

## Suggested three-hour schedule

| Activity | Approximate time | What you will do |
|---|---:|---|
| Introduction | 5 min | Review the transition from exploring data to preparing it for ML |
| **Notebook 01 — Data Cleaning** | 50 min | Identify missing, inconsistent, duplicate, and invalid values |
| **Notebook 02 — Feature Preprocessing** | 60 min | Experiment with imputation, encoding, and scaling |
| **Notebook 03 — Preprocessing Pipelines** | 55 min | Split data and build a leakage-safe preprocessing workflow |
| Wrap-up and discussion | 10 min | Review preprocessing decisions and prepare for Lab 3 |
| **Total** | **180 min** | **3 hours** |

The times are guidelines. Use extra time to finish the mini-challenges or explore how your decisions affect the prepared data.

## Notebook 01 — Data Cleaning and Quality Assessment

**File:** `01-data-cleaning.ipynb`  
**Estimated time:** 50 minutes

You will:

- Load the new apartment CSV and inspect its types and basic statistics.
- Find missing values and text accidentally entered in numerical fields.
- Convert problematic numerical strings using `pd.to_numeric(..., errors="coerce")`.
- Distinguish exact duplicate rows from conflicting records with repeated apartment IDs.
- Normalize inconsistent district labels and investigate balcony values.
- Identify physically impossible measurements and potential outliers.

**Mini-challenge:** Write a short **data-quality report** describing the issues found and how you would treat them. Explain at least one decision you would not automate without additional evidence.

**Checkpoint:** You can explain why a missing value, an invalid value, and an outlier are three different problems.

## Notebook 02 — Feature Preprocessing and Transformation

**File:** `02-feature-preprocessing.ipynb`  
**Estimated time:** 60 minutes

You will:

- Separate numerical features, categorical features, the apartment ID, and the prediction target (`monthly_rent_eur`).
- Compare **mean** and **median** imputation with `SimpleImputer`.
- Normalize categories and convert them to numerical indicators with `OneHotEncoder`.
- See how the encoder handles an unseen category using `handle_unknown="ignore"`.
- Compare `StandardScaler` and `MinMaxScaler` on numerical features.
- Apply **rule-based** type and category normalization to the actual apartment data.

Most scikit-learn transformations are taught using **small example training datasets**. We do **not** fit imputers or scalers on the whole apartment dataset: those fitted operations belong after the train/test split in Notebook 03.

**Mini-challenge:** Propose which features to impute, scale, and encode, and explain how your proposed workflow avoids data leakage.

**Checkpoint:** You can describe what `fit()`, `transform()`, and `fit_transform()` do, and which information is learned from data.

## Notebook 03 — Train/Test Splitting and Preprocessing Pipelines

**File:** `03-preprocessing-pipelines.ipynb`  
**Estimated time:** 55 minutes

You will:

- Apply consistent, deterministic cleaning rules to the raw dataset.
- Set invalid numerical feature values to missing, resolve duplicates according to the exercise rules, and exclude rows without a usable target.
- Define feature matrix `X` and rent target `y`, excluding `apartment_id` from model inputs.
- Create an 80/20 split with `train_test_split(..., random_state=42)`.
- Demonstrate how fitting preprocessing on test data can cause **data leakage**.
- Build numerical and categorical pipelines using `SimpleImputer`, `StandardScaler`, and `OneHotEncoder`.
- Combine them with `ColumnTransformer` and inspect the transformed features.

The central rule is:

```python
X_train_ready = preprocessor.fit_transform(X_train)
X_test_ready = preprocessor.transform(X_test)
```

**Mini-challenge:** Transform a new apartment with an unseen district and missing measurements using the **already fitted** preprocessor. Do not call `fit()` again.

**Checkpoint:** You can explain why a test set must not influence imputation values, scaling parameters, or learned categories.

## About the new apartment dataset

`data/apartments_corrupted.csv` contains **502 synthetic apartment records** and **9 columns**. It is a teaching dataset, not real rental-market information. It is deliberately larger and less tidy than the 150-row dataset from Lab 1.

| Column | Meaning |
|---|---|
| `apartment_id` | Apartment listing identifier |
| `area_m2` | Apartment floor area in square metres |
| `rooms` | Number of rooms |
| `building_age_years` | Age of the building in years |
| `distance_to_center_km` | Distance from the city centre in kilometres |
| `district` | District category |
| `balcony` | Whether the apartment has a balcony |
| `energy_rating` | Categorical energy rating |
| `monthly_rent_eur` | Monthly rent in euros; the future regression target |

The file contains deliberate examples of **empty fields, non-numeric strings in numeric columns, inconsistent spelling/capitalization, mixed yes/no encodings, duplicate records and IDs, invalid measurements, and unusual extreme values**.

**Do not overwrite `apartments_corrupted.csv`.** The notebooks should be able to reload the same original data. Notebook 01 emphasizes investigation, Notebook 02 explains transformations, and Notebook 03 constructs the actual training/test preprocessing workflow.

## Working with the notebooks

- Run each notebook **top to bottom**. A cell can depend on variables defined earlier in the *same* notebook.
- Complete all **Exercise** and **TODO** cells. Where requested, write your reasoning in a Markdown cell.
- **Save regularly** and copy your work to persistent storage, especially if using university lab computers that may reset between sessions.
- If a notebook state becomes confusing, restart the kernel and execute the cells again in order.
- Avoid changing or deleting the supplied CSV. Create working DataFrames in memory instead.
- A graph or transformed table is useful only when you can **explain** what it shows and why the operation was appropriate.

## What to have at the end

- `01-data-cleaning.ipynb` containing attempted exercises and a short data-quality report.
- `02-feature-preprocessing.ipynb` containing transformation experiments and a written preprocessing plan.
- `03-preprocessing-pipelines.ipynb` containing your split, the fitted preprocessing pipeline, checks of the resulting feature matrix, and a transformed new apartment.

Follow your instructor's instructions for submission. **The main learning outcome is choosing and applying appropriate transformations without leaking test information.**

## Troubleshooting

| Problem | What to check |
|---|---|
| `FileNotFoundError: data/apartments_corrupted.csv` | Open the notebook inside `lab02/` and keep `lab02/data/apartments_corrupted.csv` in place. |
| `ModuleNotFoundError: sklearn` | Launch JupyterLab using the course's `.venv` Python and check that dependencies are installed. |
| `OneHotEncoder` rejects `sparse_output` | Your scikit-learn installation may be too old for the notebook. Use the supported course environment/package versions. |
| Error involving `pd.NA` in scikit-learn categorical preprocessing | Use the missing-value conversion demonstrated in Notebook 03 before fitting the categorical imputer. |
| `NameError` for a variable from an earlier cell | Run previous cells in order or restart and run the notebook from the beginning. |
| Transformed arrays have unfamiliar column names | Inspect `preprocessor.get_feature_names_out()` and the encoder categories in Notebook 03. |
| Work is lost after logging out | Save notebooks to persistent storage or your personal device. |

For additional setup guidance, consult the course-level `README.md` in the repository root.

## Looking ahead: Lab 3

In Lab 3 we will use the **prepared apartment features** to train and evaluate a **regression model** for monthly rent. We will also introduce **classification**, where the target is a category rather than a continuous number. The preprocessing pipeline developed here will help us keep training and evaluation separate.
