import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sorting_algorithms import quick_sort, merge_sort, insertion_sort
import time
import random
from typing import List, Callable
import threading

class SortingVisualizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm ")
        self.root.geometry("1200x800")
        
        # Variables
        self.array = []
        self.sorting = False
        self.current_step = 0
        self.steps = []
        
        # Create main frames
        self.create_control_frame()
        self.create_visualization_frame()
        
        # Initialize matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(10, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.visualization_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def create_control_frame(self):
        """Create the control panel frame."""
        self.control_frame = ttk.LabelFrame(self.root, text="Controls", padding="15")
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # Array input section
        ttk.Label(self.control_frame, text="Array Input:").pack(anchor=tk.W, pady=(0, 5))
        
        # Manual input
        self.input_frame = ttk.Frame(self.control_frame)
        self.input_frame.pack(fill=tk.X, pady=5)
        ttk.Label(self.input_frame, text="Manual Input:").pack(side=tk.LEFT)
        self.array_input = ttk.Entry(self.input_frame)
        self.array_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(self.input_frame, text="Set", command=self.set_manual_array).pack(side=tk.LEFT)
        
        # Generate array section
        self.generate_frame = ttk.Frame(self.control_frame)
        self.generate_frame.pack(fill=tk.X, pady=5)
        ttk.Label(self.generate_frame, text="Size:").pack(side=tk.LEFT)
        self.size_input = ttk.Entry(self.generate_frame, width=10)
        self.size_input.pack(side=tk.LEFT, padx=5)
        
        self.case_var = tk.StringVar(value="random")
        ttk.Radiobutton(self.generate_frame, text="Random", variable=self.case_var, 
                       value="random").pack(side=tk.LEFT)
        ttk.Radiobutton(self.generate_frame, text="Sorted", variable=self.case_var, 
                       value="sorted").pack(side=tk.LEFT)
        ttk.Radiobutton(self.generate_frame, text="Reverse", variable=self.case_var, 
                       value="reverse").pack(side=tk.LEFT)
        
        ttk.Button(self.generate_frame, text="Generate", 
                  command=self.generate_array).pack(side=tk.LEFT, padx=5)
        
        # Algorithm selection
        ttk.Label(self.control_frame, text="Algorithm:").pack(anchor=tk.W, pady=(10, 5))
        self.algo_var = tk.StringVar(value="quick_sort")
        ttk.Radiobutton(self.control_frame, text="Quick Sort", variable=self.algo_var, 
                       value="quick_sort").pack(anchor=tk.W)
        ttk.Radiobutton(self.control_frame, text="Merge Sort", variable=self.algo_var, 
                       value="merge_sort").pack(anchor=tk.W)
        ttk.Radiobutton(self.control_frame, text="Insertion Sort", variable=self.algo_var, 
                       value="insertion_sort").pack(anchor=tk.W)
        
        # Speed control
        ttk.Label(self.control_frame, text="Speed:").pack(anchor=tk.W, pady=(10, 5))
        self.speed_var = tk.DoubleVar(value=0.5)
        self.speed_scale = ttk.Scale(self.control_frame, from_=0.1, to=2.0, 
                                   variable=self.speed_var, orient=tk.HORIZONTAL)
        self.speed_scale.pack(fill=tk.X)
        
        # Control buttons
        self.button_frame = ttk.Frame(self.control_frame)
        self.button_frame.pack(fill=tk.X, pady=10)
        ttk.Button(self.button_frame, text="Start", command=self.start_sorting).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.button_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
        
        # Information display (moved from right panel to bottom of control panel)
        self.info_frame = ttk.LabelFrame(self.control_frame, text="Sorting Information", padding="10")
        self.info_frame.pack(side=tk.BOTTOM, fill=tk.X, expand=True, pady=(20, 0))
        
        # Algorithm info
        self.algo_text = tk.StringVar(value="Algorithm: ")
        ttk.Label(self.info_frame, textvariable=self.algo_text, font=('Arial', 10, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        
        # Array size
        self.size_text = tk.StringVar(value="Array size: ")
        ttk.Label(self.info_frame, textvariable=self.size_text).pack(anchor=tk.W)
        
        # Time complexity info
        self.complexity_text = tk.StringVar(value="Time Complexity: ")
        ttk.Label(self.info_frame, textvariable=self.complexity_text).pack(anchor=tk.W)
        
        # Case info
        self.case_text = tk.StringVar(value="Case: ")
        ttk.Label(self.info_frame, textvariable=self.case_text).pack(anchor=tk.W)
        
        # Timing information
        ttk.Separator(self.info_frame, orient='horizontal').pack(fill=tk.X, pady=5)
        ttk.Label(self.info_frame, text="Timing Information:", font=('Arial', 9, 'bold')).pack(anchor=tk.W)
        
        self.pure_time_text = tk.StringVar(value="Pure sorting time: ")
        ttk.Label(self.info_frame, textvariable=self.pure_time_text).pack(anchor=tk.W)
        
        self.total_time_text = tk.StringVar(value="Total time: ")
        ttk.Label(self.info_frame, textvariable=self.total_time_text).pack(anchor=tk.W)
        
        self.overhead_text = tk.StringVar(value="Visualization time: ")
        ttk.Label(self.info_frame, textvariable=self.overhead_text).pack(anchor=tk.W)
        
        # Sorted array
        ttk.Separator(self.info_frame, orient='horizontal').pack(fill=tk.X, pady=5)
        self.sorted_array_text = tk.StringVar(value="Sorted array: ")
        ttk.Label(self.info_frame, textvariable=self.sorted_array_text).pack(anchor=tk.W)
        
    def create_visualization_frame(self):
        """Create the visualization frame."""
        self.visualization_frame = ttk.LabelFrame(self.root, text="Visualization", padding="15")
        self.visualization_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
    def set_manual_array(self):
        """Set array from manual input."""
        try:
            input_str = self.array_input.get()
            self.array = [int(x) for x in input_str.split()]
            self.update_visualization()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numbers separated by spaces.")
            
    def generate_array(self):
        """Generate array based on selected case and size."""
        try:
            size = int(self.size_input.get())
            case = self.case_var.get()
            
            if case == "sorted":
                self.array = list(range(1, size + 1))
            elif case == "reverse":
                self.array = list(range(size, 0, -1))
            else:  # random
                self.array = [random.randint(1, 1000) for _ in range(size)]
                
            self.update_visualization()
        except ValueError:
            messagebox.showerror("Error", "Invalid size! Please enter a number.")
            
    def update_visualization(self):
        """Update the visualization with current array state."""
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array)
        self.ax.set_title(f"Step {self.current_step}")
        self.canvas.draw()
        
    def start_sorting(self):
        """Start the sorting process."""
        if not self.array:
            messagebox.showwarning("Warning", "Please input or generate an array first!")
            return
            
        if self.sorting:
            return
            
        self.sorting = True
        self.steps = []
        self.current_step = 0
        
        # Start sorting in a separate thread
        thread = threading.Thread(target=self.sort_thread)
        thread.start()
        
    def sort_thread(self):
        """Thread function for sorting."""
        # Measure pure sorting time
        pure_start_time = time.time()
        algorithm = self.algo_var.get()
        if algorithm == "quick_sort":
            sorted_array = quick_sort(self.array.copy())
        elif algorithm == "merge_sort":
            sorted_array = merge_sort(self.array.copy())
        else:  # insertion_sort
            sorted_array = insertion_sort(self.array.copy())
        pure_sort_time = time.time() - pure_start_time
        
        # Now perform sorting with visualization
        total_start_time = time.time()
        self.array = sorted_array.copy()
        self.update_visualization()
        total_time = time.time() - total_start_time
        
        # Determine the case
        if self.array == sorted(self.array):
            case = "best"
        elif self.array == sorted(self.array, reverse=True):
            case = "worst"
        else:
            case = "average"
        
        # Update UI in the main thread
        self.root.after(0, lambda: self.update_info(
            pure_sort_time, total_time, case, sorted_array
        ))
        self.sorting = False
        
    def update_info(self, pure_sort_time, total_time, case, sorted_array):
        """Update information display."""
        algorithm = self.algo_var.get()
        n = len(self.array)
        
        # Update algorithm and size info
        self.algo_text.set(f"Algorithm: {algorithm.replace('_', ' ').title()}")
        self.size_text.set(f"Array size: {n}")
        
        # Update time complexity info
        if algorithm == "quick_sort":
            complexity = "O(n log n)" if n > 1 else "O(1)"
        elif algorithm == "merge_sort":
            complexity = "O(n log n)"
        else:  # insertion_sort
            complexity = "O(n²)"
            
        self.complexity_text.set(f"Time Complexity: {complexity}")
        self.case_text.set(f"Case: {case}")
        
        # Update timing information
        self.pure_time_text.set(f"Pure sorting time: {pure_sort_time:.6f} seconds")
        self.total_time_text.set(f"Total time: {total_time:.6f} seconds")
        self.overhead_text.set(f"Visualization time: {total_time - pure_sort_time:.6f} seconds")
        
        # Update sorted array
        self.sorted_array_text.set(f"Sorted array: {sorted_array}")
        
    def reset(self):
        """Reset the visualization."""
        self.array = []
        self.sorting = False
        self.current_step = 0
        self.steps = []
        self.update_visualization()
        
        # Reset all info displays
        self.algo_text.set("Algorithm: ")
        self.size_text.set("Array size: ")
        self.complexity_text.set("Time Complexity: ")
        self.case_text.set("Case: ")
        self.pure_time_text.set("Pure sorting time: ")
        self.total_time_text.set("Total time: ")
        self.overhead_text.set("Visualization time: ")
        self.sorted_array_text.set("Sorted array: ")
        

def main():
    root = tk.Tk()
    app = SortingVisualizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 