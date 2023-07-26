import os
import math
import time
import sys
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()

def draw_donut(A, B):
    width = 80
    height = 22
    z = [[0.0] * width for _ in range(height)]
    b = [[' '] * width for _ in range(height)]
    symbols = ".,-~:;=!*#$@"  # ASCII characters used for rendering

    for k in range(0, 628, 7):
        for j in range(0, 628, 2):
            i = j + k
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            if height > y > 0 and width > x > 0 and D > z[y][x]:
                z[y][x] = D
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                b[y][x] = symbols[N if N > 0 else 0]

    output = ''
    for y in range(height):
        for x in range(width):
            output += b[y][x]
        output += '\n'

    sys.stdout.write(output)
    sys.stdout.flush()

if __name__ == "__main__":
    A, B = 0, 0
    while True:
        clear_console()
        draw_donut(A, B)
        A += 0.04
        B += 0.08
        time.sleep(0.03)
