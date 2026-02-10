# INFO-B211 — Assignment 3: Pandas Statistical Analysis
## Iris Dataset Analyzer

---

### a) Purpose of the Program

This program analyzes Iris flower measurements using **pandas**. It loads two separate CSV files—one containing petal measurements and one containing sepal measurements—merges them into a unified dataset, and computes several statistical summaries.

The program produces the following:

#### Combined Iris Dataset
A merged CSV file containing all sepal and petal measurements for each sample.

#### Correlation Analysis
Six unique pairwise correlations between the four numeric variables:

- `sepal_length`  
- `sepal_width`  
- `petal_length`  
- `petal_width`  

#### Species‑Level Statistics
For each species (`setosa`, `versicolor`, `virginica`), the program calculates:

- Mean  
- Median  
- Standard deviation  

Each result is exported to its own CSV file for easy viewing and analysis.

The program uses a **modular, function‑based design** to keep the code organized and maintainable.

---

### b) Inputs

The program requires two CSV files located in the same directory as the script:

- `Petal_Data.csv`  
- `Sepal_Data.csv`

No user input is required. The program runs end‑to‑end automatically.

---

### c) Expected Output

The program generates the following CSV files:

#### 1. `combined_iris_data.csv`

A merged dataset containing:

- `sample_id`  
- `sepal_length`  
- `sepal_width`  
- `petal_length`  
- `petal_width`  
- `species`  

#### 2. `correlations_of_variables.csv`

A table of the six unique correlations between the four numeric variables, for example:

| variable_1     | variable_2     | Correlation |
|----------------|----------------|-------------|
| sepal_length   | sepal_width    | -0.4518     |
| sepal_length   | petal_length   | 0.7523      |
| …              | …              | …           |

#### 3. `averages_of_variables.csv`

Mean values for each variable **grouped by species**.

#### 4. `medians_of_variables.csv`

Median values for each variable **grouped by species**.

#### 5. `standard_devs_of_variables.csv`

Standard deviations for each variable **grouped by species**.

All files are saved in the script directory.

---

### d) Program Design and Implementation

The program uses a **functional design**. Each function is responsible for a specific task—loading data, merging datasets, computing correlations, computing species‑level statistics, or saving outputs. This modular structure improves readability and makes the code easier to maintain.

Below is a breakdown of each function, its purpose, inputs, and outputs.

---

## Function Documentation

### `load_data(script_dir)`

**Purpose:**  
Load the petal and sepal CSV files into pandas DataFrames.

**Input:**

- `script_dir`: directory where the script is located

**Behavior:**

- Builds file paths dynamically  
- Reads both CSV files with `pd.read_csv`

**Output:**

- `petal_df`, `sepal_df` (two DataFrames)

---

### `merge_data(petal_df, sepal_df)`

**Purpose:**  
Merge the two datasets into a single DataFrame.

**Behavior:**

- Drops the duplicate `species` column from `sepal_df`  
- Merges on `sample_id`  
- Removes any `"Unnamed"` index columns created during CSV export  

**Output:**

- `combined_df`: a clean, merged DataFrame

---

### `compute_correlations(df)`

**Purpose:**  
Compute the six unique pairwise correlations between the four numeric variables.

**Behavior:**

- Defines the six variable pairs  
- Computes Pearson correlation for each  
- Stores results in a list of dictionaries  
- Converts the list into a DataFrame

**Output:**

- DataFrame containing the six correlations

---

### `compute_species_stats(df, cols)`

**Purpose:**  
Compute mean, median, and standard deviation for each variable **grouped by species**.

**Inputs:**

- `df`: combined iris dataset  
- `cols`: list of numeric columns  

**Behavior:**  
Uses `df.groupby("species")` to compute:

- `.mean()`  
- `.median()`  
- `.std()`  

**Outputs:**

- `averages`, `medians`, `stdevs` (three DataFrames)

---

### `save_outputs(combined_df, corrs_df, averages, medians, stdevs)`

**Purpose:**  
Save all generated DataFrames to CSV files.

**Behavior:**  
Writes:

- combined dataset  
- correlations  
- averages  
- medians  
- standard deviations  

to separate CSV files.

**Output:**

- Files saved to disk  
- Confirmation message printed to terminal

---

### e) Program Flow

1. Determine the script directory using `os.path.dirname(__file__)`.  
2. Call `load_data()` to import the petal and sepal CSV files.  
3. Call `merge_data()` to create a unified iris dataset.  
4. Define the numeric columns to analyze.  
5. Call `compute_correlations()` to generate the six correlation values.  
6. Call `compute_species_stats()` to compute mean, median, and standard deviation per species.  
7. Call `save_outputs()` to write all results to CSV files.  
8. Print a final confirmation message.

---

### f) Dependencies

- `pandas` — for all data manipulation and statistical operations  
- `os` — for dynamic file path construction  
