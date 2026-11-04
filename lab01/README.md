# Lab 1 — Python Fundamentals and Exploring Data

## Learning objectives

By the end of this lab, you should be able to:

- Run Python code in a local Jupyter notebook and understand how notebook cells work.
- Use Python variables, lists, dictionaries, loops, functions, and imports.
- Create NumPy arrays and perform simple numerical calculations.
- Read a CSV file into a Pandas DataFrame, select and filter records, and compute summaries.
- Explore a dataset using histograms, bar charts, box plots, and scatter plots.
- Identify missing data and suspicious observations, and explain what you learned from the data.

**No machine-learning model is trained in Lab 1.** The aim is to understand data before attempting to prepare it for learning in Lab 2.

## Lab materials

```text
lab01/
├── README.md                       # This guide
├── 01-python-fundamentals.ipynb    # Python essentials for Java programmers
├── 02-numpy-pandas.ipynb           # Arrays, DataFrames, and CSV files
├── 03-data-exploration.ipynb       # Exploratory data analysis and plotting
└── data/
    └── apartments.csv              # Synthetic apartment listings
```

The setup scripts, dependency list, and environment-check notebook are located **one directory above** `lab01/`, at the repository root.

## Before you begin: set up your environment

Follow the **following steps** if you have yet set up the python environment.

1. Open a terminal **in the repository root**, the folder containing `requirements.txt`.
2. Run the setup script for your operating system:

   **Windows (Command Prompt or PowerShell):**

   ```bat
   setup-windows.bat
   ```

   **Linux:**

   ```bash
   bash setup-linux.sh
   ```

3. The setup script creates or reuses `.venv`, installs the initial course dependencies, and launches JupyterLab. It requires a usable local Python installation and, on first setup, usually network access for packages.
4. In JupyterLab, open **`00-environment-check.ipynb`** from the repository root and run its cells. Ask for help if a required check fails.
5. In JupyterLab's file browser, open the **`lab01/`** folder and start with `01-python-fundamentals.ipynb`.

If JupyterLab is already installed in the course virtual environment, you can launch it without repeating the installation:

```powershell
# Windows, from the repository root
.venv\Scripts\python.exe -m jupyter lab
```

```bash
# Linux, from the repository root
.venv/bin/python -m jupyter lab
```

**Important — dataset paths:** Keep `02-numpy-pandas.ipynb`, `03-data-exploration.ipynb`, and the `data/` directory together inside `lab01/`. Both data notebooks use `data/apartments.csv` as a **relative path**. In JupyterLab, open the notebooks from `lab01/`; do not move them to the repository root unless you also adjust the paths.

## Suggested three-hour schedule

| Activity | Approximate time | What you will do |
|---|---:|---|
| Setup and environment check | 25 min | Launch JupyterLab and verify libraries |
| **Notebook 01 — Python Fundamentals** | 40 min | Learn essential Python syntax through short exercises |
| **Notebook 02 — NumPy and Pandas** | 55 min | Calculate with arrays and analyze CSV records |
| **Notebook 03 — Data Exploration** | 60 min | Build plots and investigate patterns and data quality |
| Wrap-up and discussion | Remaining time | Share findings and raise questions |

The timing is a guide. If your environment is already working, use the extra time to explore the notebook challenges.

## Notebook 01 — Python Fundamentals for Java Programmers

**File:** `01-python-fundamentals.ipynb`

Work through the examples and exercises on:

- Running Python code in Jupyter.
- Variables and built-in data types.
- Lists, indexing and slicing, and dictionaries.
- Conditional statements, loops, and list comprehensions.
- Functions and importing libraries.

**Mini-challenge:** Analyze a small collection of sensor readings represented as Python dictionaries. Filter invalid observations and summarize the remaining measurements.

**Checkpoint:** You can write a small Python function and filter a list of observations without using Pandas.

## Notebook 02 — NumPy and Pandas

**File:** `02-numpy-pandas.ipynb`  
**Data:** `data/apartments.csv`

You will:

- Compare standard Python lists with NumPy arrays and vectorized calculations.
- Load the apartment CSV using `pd.read_csv()`.
- Inspect the number of records, columns, and data types.
- Select columns; filter and sort apartment listings.
- Group observations, calculate statistics, and detect missing values.

**Mini-challenge:** Investigate a claim about apartment rent using the data, and support your conclusion with a calculation.

**Checkpoint:** You can load and summarize a CSV dataset and select records that satisfy multiple conditions.

## Notebook 03 — Exploratory Data Analysis

**File:** `03-data-exploration.ipynb`  
**Data:** `data/apartments.csv`

You will:

- Examine numerical distributions with histograms and box plots.
- Compare categories using bar charts.
- Investigate numerical relationships using scatter plots and correlations.
- Identify missing values, duplicates, and potentially suspicious records.
- Explain patterns and limitations, including why correlation does not prove causation.

**Mini-challenge:** Choose an apartment-related question, create evidence for your answer, and write a short conclusion that also mentions at least one limitation.

**Checkpoint:** You can produce clear plots and explain what they do—and do not—show.

## About the apartment dataset

`data/apartments.csv` contains **150 fictional apartment listings** with **9 columns**. It is a **synthetic teaching dataset**, not real housing-market data.

| Column | Meaning |
|---|---|
| `apartment_id` | Listing identifier |
| `area_m2` | Apartment floor area in square metres |
| `rooms` | Number of rooms |
| `building_age_years` | Age of the building in years |
| `distance_to_center_km` | Distance from the city centre in kilometres |
| `district` | District category |
| `balcony` | Whether the apartment has a balcony |
| `energy_rating` | Categorical energy rating |
| `monthly_rent_eur` | Monthly rent in euros |

The dataset includes some missing values on purpose. **Do not fix or delete these records in Lab 1**: first inspect and describe them. We will discuss preprocessing choices in Lab 2. Later, `monthly_rent_eur` can serve as the target for a regression problem.

## Working in JupyterLab

- Run cells **from top to bottom**; a code cell may depend on variables from earlier cells.
- Complete the cells labelled **Exercise** or **TODO**. The notebook provides examples, but not completed exercise solutions.
- Write brief interpretations in the Markdown response areas where requested. A plot without an explanation is not a complete analysis.
- If variables become inconsistent, use **Kernel → Restart Kernel and Run All Cells** (menu wording may vary), then repeat your work.
- **Save regularly.** University lab computers may clear local work after logout. Copy your completed notebooks to persistent storage or your own device.
- If pulling updates with Git, protect modified notebooks first: updates can conflict with your local work. Consider saving working copies under different filenames.

## What to have at the end

Your completed work should include:

- `01-python-fundamentals.ipynb` with attempted exercises and mini-challenge.
- `02-numpy-pandas.ipynb` with DataFrame operations and a data-backed observation.
- `03-data-exploration.ipynb` with plots, short interpretations, and a concluding investigation.

Follow your instructor's instructions for whether and how to submit your notebooks. **The goal is understanding the data and explaining your reasoning, not just producing output.**

## Troubleshooting

| Symptom | What to check |
|---|---|
| `ModuleNotFoundError` | Start JupyterLab using `.venv`'s Python; verify the selected notebook kernel. |
| `FileNotFoundError: data/apartments.csv` | Open the notebook from `lab01/` and keep `lab01/data/apartments.csv` in place. |
| A variable such as `df` is undefined | Run earlier cells in order or restart and run all cells. |
| A plot does not appear | Run the plotting cell and check for Python errors; some notebooks require `plt.show()`. |
| Notebook changes disappear | Save copies to persistent storage before logging out. |

For detailed installation troubleshooting, see the **course-level `README.md`** in the repository root.

## Looking ahead: Lab 2

In the next lab, we will move from **exploring** data to **preparing** it for machine learning: managing missing values, encoding categories, scaling numerical features, and splitting training and test data. The apartment dataset will provide a familiar starting point.
