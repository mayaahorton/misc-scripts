import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("task_pay.csv")

# -----------------------------
# Helper: parse duration string
# -----------------------------
def duration_to_minutes(s):
    minutes = 0
    seconds = 0

    m = re.search(r"(\d+)m", s)
    s_ = re.search(r"(\d+)s", s)

    if m:
        minutes = int(m.group(1))
    if s_:
        seconds = int(s_.group(1))

    return minutes + seconds / 60


# -----------------------------
# Clean + filter data
# -----------------------------
# Exclude lower-rate extensions
df = df[df["Type"] == "Task"].copy()

# Convert duration to minutes
df["Duration_minutes"] = df["Duration"].apply(duration_to_minutes)

# Convert payable to float
df["Payable_dollars"] = (
    df["Payable"]
    .str.replace("$", "", regex=False)
    .astype(float)
)

# -----------------------------
# Linear regression
# -----------------------------
x = df["Duration_minutes"].values
y = df["Payable_dollars"].values

slope, intercept = np.polyfit(x, y, 1)

# Regression line
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = slope * x_fit + intercept

# -----------------------------
# Plot
# -----------------------------
plt.figure()
plt.scatter(x, y)
plt.plot(x_fit, y_fit)
plt.xlabel("Duration (minutes)")
plt.ylabel("Payment ($)")
plt.title("Payment vs Duration (Linear Regression)")
plt.show()

# -----------------------------
# Report results
# -----------------------------
hourly_rate = slope * 60

print(f"Slope: {slope:.4f} $/minute")
print(f"Intercept: {intercept:.4f} $")
print(f"Inferred hourly rate: ${hourly_rate:.2f} / hr")
