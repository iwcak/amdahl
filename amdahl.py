import pandas as pd

df = pd.read_csv("results/results.csv")

print("=" * 60)
print(f"{'AMDAHL LAW ANALYSIS':^60}")
print("=" * 60)

for size in ["small", "medium", "large"]:
    subset = df[df["file_size"] == size].reset_index(drop=True)
    
    t1_row = subset[subset["P"] == 1].iloc[0]
    T1 = t1_row["t_total"]
    f = t1_row["t_sort"] / T1

    print(f"\n── {size.upper()} FILE  (f = {f:.4f} = {f*100:.1f}% parallel)")
    print(f"  {'P':<6} {'T_real':>10} {'S_real':>10} {'S_amdahl':>10}")
    print(f"  {'-'*40}")

    for i in range(len(subset)):
        row = subset.iloc[i]
        P = int(row["P"])
        Tp = row["t_total"]
        S_real = T1 / Tp
        S_amdahl = 1 / ((1 - f) + f / P)
        print(f"  {P:<6} {Tp:>10.4f} {S_real:>10.4f} {S_amdahl:>10.4f}")

print("\n" + "=" * 60)
print("Critical points:")
for size in ["small", "medium", "large"]:
    subset = df[df["file_size"] == size].copy()
    T1 = subset[subset["P"] == 1]["t_total"].values[0]
    subset["speedup"] = T1 / subset["t_total"]
    best_P = subset.loc[subset["speedup"].idxmax(), "P"]
    best_S = subset["speedup"].max()
    print(f"  {size:<8} → best at P={int(best_P)}, speedup={best_S:.2f}x")