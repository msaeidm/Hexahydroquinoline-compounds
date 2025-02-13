import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy import stats

def load_in_vivo_data(file_path):
    # Expected columns: 'Group', 'Concentration', 'Survival_Days'
    return pd.read_csv(file_path)

def analyze_survival(data):
    # Calculate mean survival for each compound and concentration
    summary = data.groupby(['Group', 'Concentration'])['Survival_Days'].mean().reset_index()
    return summary

def plot_survival(summary):
    plt.figure(figsize=(8,6))
    groups = summary['Group'].unique()
    for group in groups:
        group_data = summary[summary['Group'] == group]
        plt.plot(group_data['Concentration'], group_data['Survival_Days'], marker='o', label=group)
    plt.xlabel('Concentration (μg/mL)')
    plt.ylabel('Mean Survival (Days)')
    plt.title('In Vivo Mice Survival Analysis')
    plt.legend()
    plt.grid(True)
    os.makedirs("../results/figures", exist_ok=True)
    plt.savefig("../results/figures/in_vivo_survival.png")
    plt.close()

def perform_statistics(data):
    # For demonstration, perform one-way ANOVA comparing survival between groups at a given concentration
    # Here we assume the data is structured appropriately
    concentration = data['Concentration'].unique()[0]
    subset = data[data['Concentration'] == concentration]
    groups = subset.groupby('Group')
    survival_data = [group['Survival_Days'].values for name, group in groups]
    F, p = stats.f_oneway(*survival_data)
    return F, p

def main():
    file_path = "../data/bioactivity/in_vivo_survival.csv"
    data = load_in_vivo_data(file_path)
    summary = analyze_survival(data)
    plot_survival(summary)
    F, p = perform_statistics(data)
    print(f"ANOVA F-statistic: {F:.2f}, p-value: {p:.4f}")
    os.makedirs("../results/tables", exist_ok=True)
    summary.to_csv("../results/tables/in_vivo_summary.csv", index=False)
    with open("../results/tables/in_vivo_stats.txt", "w") as f:
        f.write(f"ANOVA F-statistic: {F:.2f}, p-value: {p:.4f}\n")
    print("In vivo analysis completed and results saved.")

if __name__ == "__main__":
    main()
