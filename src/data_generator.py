import pandas as pd
import numpy as np

def generate_data(n=500):
    np.random.seed(42)

    data = pd.DataFrame({
        "Age": np.random.randint(22, 60, n),
        "Experience": np.random.randint(1, 20, n),
        "Salary": np.random.randint(30000, 150000, n),
        "TrainingHours": np.random.randint(10, 100, n),
        "Department": np.random.choice(["HR", "IT", "Sales"], n)
    })

    # Add noise for realism
    random_factor = np.random.rand(n)

    data["Performance"] = np.where(
        (data["Experience"] > 10) & (data["TrainingHours"] > 60) & (random_factor > 0.3),
        "High",
        np.where(
            (data["Experience"] > 5) & (random_factor > 0.2),
            "Medium",
            "Low"
        )
    )

    return data