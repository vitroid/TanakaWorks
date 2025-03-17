# 添付はcontour mapの元データです。描いてみてもらえませんか。
# 各行はx, y, z, w, yeであって、(x,y)に対して、zかwが高さです。また、yは圧力の対数で、yeが圧力です。
# zは水との平衡にあるハイドレートが生成するとき、wはゲスト流体と平衡にあるハイドレートが生成するときの駆動力です。
# 追伸。xは▼温度
# 読みこむデータファイル名は"contour_ch4.d"です。
# プログラムの先頭に、私の入力したプロンプトを全部コメントとして書き加えて下さい。また、等高線を色彩だけでなく、線と標高値も含めて描いて下さいね。

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata


def generate_contour_levels(data):
    """
    0 を含み、等間隔で小数点2桁目以下が 0 であるような等高線レベルを生成する。

    Args:
        data: z と w の値のリストまたは NumPy 配列。

    Returns:
        等高線レベルのリスト。
    """

    # 1. z と w の最小値と最大値を求める
    min_val = np.min(data)
    max_val = np.max(data)

    # 2. 等高線の間隔を決定
    # 適切な間隔を自動で決定するロジックを実装することも可能ですが、ここでは例として 0.1, 0.2, 1.0, 2.0 などの間隔を想定します。
    # 最小値と最大値から適切な間隔を決定するロジックを組み込むとより汎用性が高まります。
    # ここでは、最大値と最小値の差が1未満なら0.1, 10未満なら1, 100未満なら10, それ以上なら100の間隔とする例
    diff = max_val - min_val
    if diff < 1:
        interval = 0.01
    elif diff < 10:
        interval = 0.1
    elif diff < 100:
        interval = 1.0
    else:
        interval = 10.0

    # 3. 0 を含む等高線レベルを生成
    levels = []
    # 負の方向
    current_level = 0.0
    while current_level >= min_val:
        levels.append(current_level)
        current_level -= interval
        if current_level < min_val:
            levels.append(min_val)
            break
    levels.reverse()

    # 正の方向
    current_level = interval
    while current_level <= max_val:
        if current_level not in levels:
            levels.append(current_level)
        current_level += interval
        if current_level > max_val:
            if max_val not in levels:
                levels.append(max_val)
            break

    # 0がなければ追加
    if 0 not in levels:
        levels.insert(0, 0)

    # 重複を削除
    levels = sorted(list(set(levels)))

    return levels


def plot_contour(filepath, suptitle=""):
    """
    Reads data from a file, and plots two contour maps:
    - One for the 'z' values (hydrates in equilibrium with water).
    - One for the 'w' values (hydrates in equilibrium with guest fluid).
    Displays filled contours, contour lines, and elevation labels.
    Adds hatching to the areas where z or w is exactly 0.

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

    # 等高線レベルを生成
    levels_z = generate_contour_levels(Z)
    levels_w = generate_contour_levels(W)

    # 正のレベルを削除
    levels_z_filtered = [level for level in levels_z if level <= 0]
    levels_w_filtered = [level for level in levels_w if level <= 0]

    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Contour plot for z
    contourf_z = axes[0].contourf(X, Y, Z, levels=levels_z, cmap="viridis")
    # 等高線の色を制御
    colors_z = ["white" for level in levels_z_filtered]
    contour_z = axes[0].contour(X, Y, Z, levels=levels_z_filtered, colors=colors_z)
    # 等高線のラベルの色を制御
    axes[0].clabel(contour_z, inline=True, fontsize=8, fmt="%1.1f")
    axes[0].set_title("Hydrate Equilibrium with Water (z)")
    axes[0].set_xlabel("Temperature (x)")
    axes[0].set_ylabel("log(Pressure) (y)")
    fig.colorbar(contourf_z, ax=axes[0], label="z (Driving Force)")

    # Set the x-axis limit for the z plot
    axes[0].set_xlim(left=220)

    # Contour plot for w
    contourf_w = axes[1].contourf(X, Y, W, levels=levels_w, cmap="viridis")
    # 等高線の色を制御
    colors_w = ["white" for level in levels_w_filtered]
    contour_w = axes[1].contour(X, Y, W, levels=levels_w_filtered, colors=colors_w)
    axes[1].clabel(contour_w, inline=True, fontsize=8, fmt="%1.1f")
    axes[1].set_title("Hydrate Equilibrium with Guest Fluid (w)")
    axes[1].set_xlabel("Temperature (x)")
    axes[1].set_ylabel("log(Pressure) (y)")
    fig.colorbar(contourf_w, ax=axes[1], label="w (Driving Force)")

    # Set the x-axis limit for the w plot
    axes[1].set_xlim(left=220)

    plt.tight_layout()
    # plt.suptitle("Hydrate Equilibrium", fontsize=16)
    plt.suptitle(suptitle, fontsize=16)
    # plt.show()

    # you can save the plot to a file.
    plt.savefig(filepath + ".pdf")


# Call the function with the specified filename
plot_contour("contour_ch4.d", "Methane")
plot_contour("contour_co2.d", "CO2")
