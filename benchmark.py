import csv
import os
from main import run

FILES = {
    "small":  "data/small.txt",
    "medium": "data/medium.txt",
    "large":  "data/large.txt",
}
P_VALUES = [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    os.makedirs("results", exist_ok=True)

    with open("results/results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["file_size", "P", "t_split", "t_sort", "t_merge", "t_total"])

        for size_name, filepath in FILES.items():
            for P in P_VALUES:
                print(f"Running {size_name} | P={P}")
                t_split, t_sort, t_merge, t_total = run(filepath, P)
                writer.writerow([size_name, P,
                                 round(t_split, 6),
                                 round(t_sort, 6),
                                 round(t_merge, 6),
                                 round(t_total, 6)])

    print("\nDone! Results saved to results/results.csv")