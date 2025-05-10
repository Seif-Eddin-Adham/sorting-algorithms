# Sorting Algorithms Analysis Project

This project implements and analyzes the performance of three popular sorting algorithms:
- Quick Sort
- Merge Sort
- Insertion Sort

## Features

- **Interactive Command-Line Visualizer** (`interactive_sorting.py`):
  - Choose to input an array manually or generate best, worst, or average case arrays.
  - Select sorting algorithm (Quick Sort, Merge Sort, Insertion Sort).
  - Step-by-step visualization (matplotlib) of the sorting process.
  - Shows pure sorting time, total time (with visualization), visualization overhead, time complexity, and case.

- **Graphical User Interface (GUI) Visualizer** (`sorting_visualizer_gui.py`):
  - User-friendly GUI built with Tkinter and Matplotlib.
  - Input arrays manually or generate them (random, sorted, reverse).
  - Select sorting algorithm and control visualization speed.
  - All sorting information (algorithm, array size, time complexity, case, pure sorting time, total time, visualization overhead, sorted array) is displayed at the bottom of the left control panel, under the controls.
  - Large, central visualization area for the sorting process.

- **Performance Analysis** (`performance_analysis.py`):
  - Compares the performance of all algorithms on different array sizes and cases.
  - Generates a performance graph (`sorting_performance.png`).

## Time Complexity Analysis

### Quick Sort
- Best Case: O(n log n) - When the pivot divides the array into roughly equal parts
- Average Case: O(n log n)
- Worst Case: O(n²) - When the array is already sorted or reverse sorted

### Merge Sort
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)
- Space Complexity: O(n)

### Insertion Sort
- Best Case: O(n) - When the array is already sorted
- Average Case: O(n²)
- Worst Case: O(n²) - When the array is reverse sorted

## Project Structure

- `sorting_algorithms.py`: Contains the implementation of all three sorting algorithms
- `interactive_sorting.py`: Interactive command-line visualizer
- `Sorting_GUI.py`: Graphical user interface visualizer (Tkinter + Matplotlib)
- `performance_reference.py`: Performance analysis and comparison
- `performance_reference.png`: Generated graph showing the performance comparison

## Requirements

- Python 3.6+
- matplotlib
- numpy
- tkinter (usually included with Python)

Install the required packages using:
```bash
pip install matplotlib numpy
```

## Usage

### Run the GUI Visualizer
```bash
python sorting_visualizer_gui.py
```
- Use the left panel to input or generate arrays, select the algorithm, and control speed.
- Click **Start** to visualize the sorting process.
- All sorting and timing information will appear at the bottom of the left panel.

### Run the Command-Line Visualizer
```bash
python interactive_sorting.py
```
- Follow the prompts to input/generate arrays and select algorithms.
- Step-by-step visualization and detailed timing info will be shown in the terminal and matplotlib window.

### Run the Performance Analysis
```bash
python performance_analysis.py
```
- Compares all algorithms on different cases and array sizes.
- Generates `sorting_performance.png` with performance graphs.

## Results

The performance analysis will generate a graph (`sorting_performance.png`) showing:
- Performance comparison for random arrays
- Performance comparison for sorted arrays
- Performance comparison for reverse-sorted arrays

Each graph shows the execution time for different array sizes, allowing you to visualize how each algorithm performs under different conditions.

---

**Enjoy exploring and visualizing sorting algorithms!** 