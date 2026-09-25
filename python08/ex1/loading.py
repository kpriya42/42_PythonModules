#!/usr/bin/env python3

import importlib.metadata
import sys


def analyze_data() -> None:
    import pandas as pd  # type: ignore[import-untyped]
    import numpy as np   # type: ignore[import-not-found]
    import matplotlib.pyplot as plt   # type: ignore[import-not-found]

    print("\nAnalyzing Matrix data...")
    n = 1000
    values = np.random.uniform(10.0, 100.0, size=n)

    print(f"Processing {n} data points...")
    data = pd.DataFrame({"Value": values})
    print(data["Value"].describe())
    # Calculate a moving average over every 50 points
    data["Moving Average"] = data["Value"].rolling(window=50).mean()

    print("\nGenerating visualization...")
    plt.plot(data.index.to_numpy(), data["Value"].to_numpy(),
             label="Original Data", marker="o", color="orange")
    plt.plot(data.index.to_numpy(), data["Moving Average"].to_numpy(),
             label="50-point Moving Average")

    # Newer tool versions
    # plt.plot(data.index, data["Value"], label="Original Data",
    #         marker="o", color="orange")   # type: ignore[import-untyped]
    # plt.plot(data.index, data["Moving Average"],
    #         label="50-point Moving Average")

    plt.title("Analysis of 1000 Random Data Points")
    plt.xlabel("Data Point")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()
    plt.savefig("matrix_analysis.png", dpi=300)
    plt.show()
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def check_dependencies(packages: list[tuple[str, str]]) -> bool:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    missing = False
    for package, info in packages:
        try:
            package_version = importlib.metadata.version(package)
            print(f"[OK] {package} ({package_version}) - {info}")
        except Exception:
            missing = True
            print(f"[MISSING] {package} - Not ready")
    if missing is True:
        print("\nInstall missing dependencies in venv with pip:",
              "   python3 -m pip install -r requirements.txt",
              "and run the program again.", sep='\n')
    return (missing)


def main() -> None:
    if (sys.prefix == sys.base_prefix):
        print("Run the program in a virtual environment.",
              "This program needs some specific tools versions that"
              "may not be necessary in the global environment.", "",
              "Manual Virtual environment creation using:",
              "  python3 -m venv matrix_env",
              "  source matrix_env/bin/activate",
              "  python3 loading.py", "or",
              "Automatic Virtual environment creation & dependency"
              " installation using poetry:",
              "  poetry install",
              "  poetry run python3 loading.py", sep='\n')
    else:
        packages = [("pandas", "Data manipulation ready"),
                    ("numpy", "Numerical computation ready"),
                    ("matplotlib", "Visualization ready")]
        missing = check_dependencies(packages)
        if not missing:
            analyze_data()


if __name__ == "__main__":
    main()
