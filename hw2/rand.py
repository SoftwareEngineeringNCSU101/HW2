"""
This module generates an array of random integers.
"""
# rand.py

import subprocess

def random_array(arr):
    """Generates an array of random integers."""
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, text=True, check=True)
        arr[i] = int(shuffled_num.stdout.strip())
    return arr
