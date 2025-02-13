import pandas as pd
import matplotlib.pyplot as plt

def analyze_flow_cytometry(file_path):
    # Example: Load a CSV file containing % mortality data for different compound concentrations.
    data = pd.read_csv(file_path)
    # Assume data has columns: 'Concentration', 'Z1', 'Z2', 'Z3', 'Z4', 'DMSO', 'Saponin'
    return data

def plot_mortality(data):
    plt.figure(figsize=(8,6))
    for compound in ['Z1', 'Z2', 'Z3', 'Z4']:
        plt.plot(data['Concentration'], data[compound], marker='o', label=compound)
    plt.xlabel('Concentration (μg/mL)')
    plt.ylabel('Tachyzoite Mortality (%)')
    plt.title('Flow Cytometry Analysis of T. gondii Tachyzoite Mortality')
    plt.legend()
    plt.grid(True)
    plt.savefig('../results/figures/mortality_plot.png')
    plt.show()

def main():
    data = analyze_flow_cytometry('../data/bioactivity/flow_cytometry.csv')
    plot_mortality(data)
    # Save summary table
    data.to_csv('../results/tables/flow_cytometry_summary.csv', index=False)

if __name__ == "__main__":
    main()
