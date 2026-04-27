# 🫀 Heart Disease Analysis — Data Science Mini Project

A Python-based Data Science mini-project developed as part of the **Master's program in Computer Science and Artificial Intelligence** at **Ibn Tofail Faculty, Kenitra, Morocco**.

---

## 📋 Project Overview

This project performs a complete analysis of a real-world **Heart Disease dataset** using Python and key data science libraries (NumPy, Pandas, Matplotlib). It covers data loading, cleaning, exploratory analysis, and visualization.

---

## 📁 Project Structure

```
data-science-mini-project-python/
│
├── data/
│   ├── processed/
│   │   └── dataset_clean.csv        # Cleaned dataset after preprocessing
│   └── raw/
│       └── data_set.csv             # Original raw dataset
│
├── notebooks/
│   ├── 01_load_dataset.ipynb        # Data loading and first exploration
│   └── 02_clean_dataset.ipynb       # Data cleaning and preprocessing
│
├── outputs/
│   └── figures/                     # Generated plots and visualizations
│
├── src/
│   ├── __init__.py
│   ├── analyzer.py                  # Statistical analysis and groupby logic
│   ├── cleaner.py                   # Data cleaning functions
│   ├── data_explorer.py             # Exploratory data analysis (EDA)
│   ├── data_loader.py               # Dataset loading utilities
│   └── visualizer.py               # Plotting and chart generation
│
├── venv/                            # Python virtual environment (not tracked)
├── .gitignore
├── LICENSE
├── main.py                          # Entry point of the project
├── makefile                         # Automation commands
├── README.md
└── requirements.txt                 # Python dependencies
```

---

## 🗂️ Dataset

**Source:** [Kaggle / UCI Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

The dataset contains medical variables related to heart disease analysis. It includes **1000+ rows** and the following key variables:

| Column | Description |
|---|---|
| `age` | Age of the patient |
| `sex` | Sex of the patient (0 = female, 1 = male) |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol level (mg/dl) |
| `thalach` | Maximum heart rate achieved |
| `oldpeak` | ST depression induced by exercise |
| `target` | Target variable — 1 = heart disease, 0 = no heart disease |

---

## 🔬 Work Done

### 1. Data Loading
- Import of the raw dataset
- Display of the first rows for initial exploration

### 2. Data Cleaning
- Handling missing values
- Removal of duplicate rows
- Verification and correction of data types

### 3. Data Analysis
- Descriptive statistics (mean, std, min, max, quartiles)
- Group-based analysis using `groupby`
- Identification of trends and correlations with the target variable

### 4. Visualization
- Distribution plots for key variables
- Correlation heatmap
- Group comparison charts saved to `outputs/figures/`

### 5. Interpretation
- Explanation of results obtained
- Relevant conclusions about risk factors linked to heart disease

---

## ⚙️ Setup & Usage

### Prerequisites

- Python 3.8+
- pip

### Install Dependencies

```bash
make install
```

Or manually:

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
make run
```

Or directly:

```bash
python3 main.py
```

### Clean Cache

```bash
make clean
```

---

## 🛠️ Makefile Reference

```makefile
PYTHON = python3
MAIN = main

install:
    pip install -r requirements.txt

run:
    $(PYTHON) $(MAIN)

clean:
    rm -rf __pycache__
    rm -f .pyc

.PHONY: install run test clean
```

---

## 📦 Requirements

Key libraries used (see `requirements.txt` for full list):

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `jupyter`

---

## 👥 Authors

Developed as part of a group project (1–3 students) for the Master's program in **Computer Science and Artificial Intelligence** — Ibn Tofail Faculty, Kenitra, Morocco.

---

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.