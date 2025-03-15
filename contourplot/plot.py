# 添付はcontour mapの元データです。描いてみてもらえませんか。
# 各行はx, y, z, w, yeであって、(x,y)に対して、zかwが高さです。また、yは圧力の対数で、yeが圧力です。
# zは水との平衡にあるハイドレートが生成するとき、wはゲスト流体と平衡にあるハイドレートが生成するときの駆動力です。
# 追伸。xは▼温度
# 読みこむデータファイル名は"contour_ch4.d"です。
# プログラムの先頭に、私の入力したプロンプトを全部コメントとして書き加えて下さい。また、等高線を色彩だけでなく、線と標高値も含めて描いて下さいね。

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata


def plot_contour(filepath):
    """
    Reads data from a file, and plots two contour maps:
    - One for the 'z' values (hydrates in equilibrium with water).
    - One for the 'w' values (hydrates in equilibrium with guest fluid).
    Displays filled contours, contour lines, and elevation labels.

    Args:
        filepath: The path to the data file.
    """
    try:
        data = np.loadtxt(filepath)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    x = data[:, 0]  # Temperature (x)
    y = data[:, 1]  # log(Pressure) (y)
    z = data[:, 2]  # Hydrate equilibrium with water (z)
    w = data[:, 3]  # Hydrate equilibrium with guest fluid (w)
    ye = data[:, 4]  # Pressure (not directly used for contour, but available)

    # Create a grid for contour plotting
    xi = np.linspace(x.min(), x.max(), 100)
    yi = np.linspace(y.min(), y.max(), 100)
    X, Y = np.meshgrid(xi, yi)

    # Interpolate z and w onto the grid
    Z = griddata((x, y), z, (X, Y), method="linear")
    W = griddata((x, y), w, (X, Y), method="linear")

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Contour plot for z
    contourf_z = axes[0].contourf(X, Y, Z, cmap="viridis")
    contour_z = axes[0].contour(X, Y, Z, colors="black")  # Contour lines
    axes[0].clabel(contour_z, inline=True, fontsize=8, fmt="%1.1f")  # Elevation labels
    axes[0].set_title("Hydrate Equilibrium with Water (z)")
    axes[0].set_xlabel("Temperature (x)")
    axes[0].set_ylabel("log(Pressure) (y)")
    fig.colorbar(contourf_z, ax=axes[0], label="z (Driving Force)")

    # Contour plot for w
    contourf_w = axes[1].contourf(X, Y, W, cmap="viridis")
    contour_w = axes[1].contour(X, Y, W, colors="black")  # Contour lines
    axes[1].clabel(contour_w, inline=True, fontsize=8, fmt="%1.1f")  # Elevation labels
    axes[1].set_title("Hydrate Equilibrium with Guest Fluid (w)")
    axes[1].set_xlabel("Temperature (x)")
    axes[1].set_ylabel("log(Pressure) (y)")
    fig.colorbar(contourf_w, ax=axes[1], label="w (Driving Force)")

    plt.tight_layout()
    plt.suptitle("Hydrate Equilibrium", fontsize=16)
    plt.show()

    # you can save the plot to a file.
    # plt.savefig("contour_plots.png")


# Call the function with the specified filename
plot_contour("contour_ch4.d")
