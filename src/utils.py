import os
import matplotlib.pyplot as plt

FIGURES_DIR = "../reports/figures"

def save_figure(filename):
    """Save the current matplotlib chart to reports/figures/."""
    os.makedirs(FIGURES_DIR, exists_ok=True)
    plt.savefig(os.path.join(FIGURES_DIR, filename), dpi=150, bbox_inches="tight")
    print(f"Figure Saved: {filename}")


def profile_dataframe(df):
    """Print a quick summary of any DataFrame."""
    print(f"Rows        : {df.shape[0]:,}")
    print(f"Columns     : {df.shape[1]}")
    print(f"Null cells  : {df.isnull().sum().sum():,}")
    print(f"Duplicates  : {df.duplicated().sum():,}")
