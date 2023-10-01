import sys
import math
import shutil
from time import time
from config import tqdm_config


def calculate_non_bar_width(i, total, elapsed_time, speed):
    percentage_width = len(f"{math.floor(i/total * 100)}%")
    item_info_width = len(f" {i}/{total}")
    time_info_width = len(
        f" [{math.floor(elapsed_time / 60):02}:{(math.floor(elapsed_time) % 60):02}<{(math.floor((total-i)/speed / 60)):02}:{(math.floor((total-i)/speed) % 60):02} , {speed:.2f}it/s]")
    return percentage_width + item_info_width + time_info_width + len(tqdm_config["opening_char"]) + len(tqdm_config["closing_char"])


def ft_tqdm(lst: range) -> None:
    start_time = time()
    total = len(lst)
    width_offset = 42
    n_bars = shutil.get_terminal_size().columns - width_offset

    for i, item in enumerate(lst, 1):

        elapsed_time = time() - start_time
        speed = i / elapsed_time
        current_bars = math.floor(i/total * n_bars)

        width_offset = calculate_non_bar_width(i, total, elapsed_time, speed)
        n_bars = shutil.get_terminal_size().columns - width_offset

        bar_string = tqdm_config["opening_char"] + (tqdm_config["elapsed_char"] * current_bars) + (tqdm_config["undone_char"] *
                                                                                                   (n_bars - current_bars)) + tqdm_config["closing_char"]

        sys.stdout.write(
            "\r" + f"{math.floor(i/total * 100)}%" + bar_string + f" {i}/{total}" + f" [{math.floor(elapsed_time / 60):02}:{(math.floor(elapsed_time) % 60):02}<{(math.floor((total-i)/speed / 60)):02}:{(math.floor((total-i)/speed) % 60):02}, {speed:.2f}it/s]")
        sys.stdout.flush()
        # width_offset = len(bar_string) - (n_bars + 2)
        # width_offset = 42

        yield item