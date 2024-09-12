"""
This module provides a function to create an array of random numbers using the `shuf` command.
"""

import subprocess  # nosec


def random_array(arr):
    """
    Populates the given array with random numbers using the 'shuf' command.

    Args:
        arr (list): List to populate with random numbers.

    Returns:
        list: List populated with random numbers.
    """
    shuf_command = "/usr/bin/shuf"  # Specify the full path to the shuf command
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            [shuf_command, "-i1-20", "-n1"], capture_output=True, check=True)  # nosec
        arr[i] = int(shuffled_num.stdout)
    return arr
