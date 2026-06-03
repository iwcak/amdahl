import multiprocessing
import time

from s_sort import selection_sort

def split_phase(filename, P):
    t_start = time.perf_counter()
    with open(filename, 'r') as f:
        lines = [int(x.strip()) for x in f.readlines()]
    
    chunk_size = len(lines) // P
    chunks = []
    for i in range(P):
        if i == P - 1:
            chunks.append(lines[i * chunk_size:])  # last chunk gets remainder
        else:
            chunks.append(lines[i * chunk_size : (i + 1) * chunk_size])
    
    t_end = time.perf_counter()
    return chunks, t_end - t_start


def sort_phase(chunks, P):
    t_start = time.perf_counter()
    with multiprocessing.Pool(processes=P) as pool:
        sorted_chunks = pool.map(selection_sort, chunks)
    t_end = time.perf_counter()
    return sorted_chunks, t_end - t_start


def merge_phase(sorted_chunks):
    import heapq
    t_start = time.perf_counter()
    merged = list(heapq.merge(*sorted_chunks))
    t_end = time.perf_counter()
    return merged, t_end - t_start


def run(filename, P):
    chunks, t_split = split_phase(filename, P)
    sorted_chunks, t_sort = sort_phase(chunks, P)
    merged, t_merge = merge_phase(sorted_chunks)
    t_total = t_split + t_sort + t_merge

    print(f"P={P} | split={t_split:.4f}s | sort={t_sort:.4f}s | merge={t_merge:.4f}s | total={t_total:.4f}s")
    return t_split, t_sort, t_merge, t_total


if __name__ == "__main__":
    run("data/small.txt", P=2)