<div align="center"> 
  <h1> Binomial Option Pricing Model </h1>
  <h3> Stock Option Pricing & Analysis </h3>

![Python](https://img.shields.io/badge/Language-Python%203.x-blue?logo=python&logoColor=white)
![Numpy](https://img.shields.io/badge/Library-Numpy-orange?logo=numpy)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-ff69b4?logo=matplotlib)
![yfinance](https://img.shields.io/badge/Data%20Source-yfinance-4E9A06?logo=python)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?logo=windows)

</div>

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [Authors](#authors)

---

## Overview

This project is an **implementation of a stock option pricing model using the Binomial Option Pricing Model (BOPM)**. All detailed explanations regarding the theory, algorithm, and result analysis can be found in the paper PDF file inside the `doc/` folder.

---

### Tech Stack

- Language: **Python 3.x**
- Libraries: **Numpy**, **Pandas**, **Matplotlib**, **yfinance**
- Platform: **Cross-platform (Windows, Mac, Linux)**

---

### Folder Structure

- Preprocessing & model: `src/`
- Preprocessed data: `data/variables_output/`
- Documentation & paper: `doc/`
- Example input/output: `data/`
- Requirements file: `requirements.txt`

---

## Getting Started

1. **Install Python 3.x** and pip
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run preprocessing and model respectively:

```bash
cd src
python preprocess_variables.py
python binomial_model.py
python discrete_steps_test.py
```

---

## Authors

| Name                     | NIM      |
| ------------------------ | -------- |
| Nathaniel Jonathan Rusli | 13523013 |

---

> **Note:**
> For a complete explanation of the theory, algorithm, and result analysis, please refer to the paper in the `doc/` folder.
