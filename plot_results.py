import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")
P_VALUES = [1, 2, 3, 4, 5, 6, 7, 8]

for size in ["small", "medium", "large"]:
    t1 = df[(df["file_size"] == size) & (df["P"] == 1)]["t_total"].values[0]
    df.loc[df["file_size"] == size, "speedup"] = t1 / df[df["file_size"] == size]["t_total"]

fig, ax = plt.subplots(figsize=(9, 6))

ax.plot(P_VALUES, P_VALUES, "k--", linewidth=1.5, label="Ideal (linear)")
colors = {"small": "tomato", "medium": "orange", "large": "steelblue"}
for size in ["small", "medium", "large"]:
    subset = df[df["file_size"] == size]
    ax.plot(subset["P"], subset["speedup"], marker="o", linewidth=2,
            color=colors[size], label=f"{size.capitalize()} file")

ax.set_xlabel("Number of processes (P)", fontsize=12)
ax.set_ylabel("Speedup  Sp = T1 / Tp", fontsize=12)
ax.set_title("Speedup vs Number of Processes (Amdahl's Law)", fontsize=14)
ax.legend(fontsize=11)
ax.set_xticks(P_VALUES)
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("results/speedup_chart.png", dpi=150)
print("Saved speedup_chart.png")

fig, axes = plt.subplots(1, 3, figsize=(14, 5), sharey=False)

for ax, size in zip(axes, ["small", "medium", "large"]):
    subset = df[df["file_size"] == size]
    ax.bar(subset["P"], subset["t_split"], label="Split", color="lightblue")
    ax.bar(subset["P"], subset["t_sort"],  bottom=subset["t_split"], label="Sort", color="steelblue")
    ax.bar(subset["P"], subset["t_merge"], bottom=subset["t_split"]+subset["t_sort"], label="Merge", color="navy")
    ax.set_title(f"{size.capitalize()} file", fontsize=12)
    ax.set_xlabel("P")
    ax.set_ylabel("Time (s)")
    ax.set_xticks(P_VALUES)
    ax.legend(fontsize=9)

plt.suptitle("Time Breakdown per Phase", fontsize=14)
plt.tight_layout()
plt.savefig("results/time_breakdown.png", dpi=150)
print("Saved time_breakdown.png")

plt.show()