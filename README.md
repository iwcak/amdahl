## Description
This project implements a parallel file sorting program in Python
and analyzes its scalability using Amdahl's Law.

The program processes a data file in three phases:
- **Split** — sequentially divides the file into P equal chunks
- **Sort** — each chunk is sorted in parallel using Selection Sort O(n²)
- **Merge** — sorted chunks are merged back into one file sequentially
## How to run:
git clone https://github.com/iwcak/amdahl

pip install -r requirements.txt 

(pip install pandas matplotlib)

python gen_data.py

python benchmark.py

python plot_results.py

python amdahl.py
