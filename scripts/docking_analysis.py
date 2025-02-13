import pandas as pd
import matplotlib.pyplot as plt

def parse_docking_results(file_path):
    # Example: Read a CSV file containing docking energies for each compound.
    docking_data = pd.read_csv(file_path)
    # Assume columns: 'Compound', 'Binding_Energy'
    return docking_data

def plot_docking(docking_data):
    plt.figure(figsize=(6,4))
    plt.bar(docking_data['Compound'], docking_data['Binding_Energy'], color='skyblue')
    plt.xlabel('Compound')
    plt.ylabel('Binding Energy (kcal/mol)')
    plt.title('Docking Analysis of 5-oxo-hexahydroquinolines')
    plt.savefig('../results/figures/docking_barplot.png')
    plt.show()

def main():
    docking_data = parse_docking_results('../data/docking/docking_results.csv')
    plot_docking(docking_data)
    docking_data.to_csv('../results/tables/docking_summary.csv', index=False)

if __name__ == "__main__":
    main()
