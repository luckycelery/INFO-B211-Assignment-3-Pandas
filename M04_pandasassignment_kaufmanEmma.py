import pandas as pd
import os

# -----------------------------
# Load Data
# -----------------------------
def load_data(script_dir):
    #load data files with dynamic pathing
    petal_file = os.path.join(script_dir, "Petal_Data.csv")
    sepal_file = os.path.join(script_dir, "Sepal_Data.csv")

    #read the datafiles and return their contents 
    petal_df = pd.read_csv(petal_file)
    sepal_df = pd.read_csv(sepal_file)

    return petal_df, sepal_df


# -----------------------------
# Merge Data
# -----------------------------
def merge_data(petal_df, sepal_df):
    combined = pd.merge(
        petal_df,
        #remove one of the species columns or else repeats
        sepal_df.drop(columns=["species"]),
        #defines what it is combining based on
        on="sample_id",
    )

    # remove leftover index columns if present
    cols_to_drop = [col for col in combined.columns if col.startswith("Unnamed")]
    combined_df = combined.drop(columns=cols_to_drop)

    #returns the combined data frame 
    return combined_df


# -----------------------------
# Compute Statistics
# -----------------------------
def compute_correlations(df):
    #states all the pairs of attributes 
    pairs = [
        ("sepal_length", "sepal_width"),
        ("sepal_length", "petal_length"),
        ("sepal_length", "petal_width"),
        ("sepal_width", "petal_length"),
        ("sepal_width", "petal_width"),
        ("petal_length", "petal_width"),
    ]
    #empty list to hold new correlations
    results = []
    #goes through each pair in the key value list
    for a, b in pairs:
        corr = df[a].corr(df[b])
        results.append({"variable_1": a, "variable_2": b, "Correlation": corr})
    #turns the list into a dataframe format
    return pd.DataFrame(results)


def compute_species_stats(df, cols):
    #computes mean median and stdev of each of the species for each of the attributes
    averages = df.groupby("species")[cols].mean()
    medians = df.groupby("species")[cols].median()
    stdevs = df.groupby("species")[cols].std()
    return averages, medians, stdevs


# -----------------------------
# Save Outputs
# -----------------------------
def save_outputs(combined_df, corrs_df, averages, medians, stdevs):
    #saves each of the outputs to their own files 
    combined_df.to_csv("combined_iris_data.csv", index=False)
    corrs_df.to_csv("correlations_of_variables.csv", index=False)
    averages.to_csv("averages_of_variables.csv", index=True)
    medians.to_csv("medians_of_variables.csv", index=True)
    stdevs.to_csv("standard_devs_of_variables.csv", index=True)

    print("All output files created successfully.")


# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    #dynamic pathic setup for script's directory
    script_dir = os.path.dirname(__file__)
    #call for the data to be loaded into the program 
    petal_df, sepal_df = load_data(script_dir)
    #take the ouut of load_data and merge it into a single df and returns it 
    combined_df = merge_data(petal_df, sepal_df)
    #define the columns that we are looking at 
    cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    #call for correlational data to be calculated based off of the combined dataframe 
    corrs_df = compute_correlations(combined_df)
    #calls for other stats for each species
    averages, medians, stdevs = compute_species_stats(combined_df, cols)
    #calls for the saving of each of the outputs
    save_outputs(combined_df, corrs_df, averages, medians, stdevs)
