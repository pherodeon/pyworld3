# -*- coding: utf-8 -*-
# %%
# Libraries
import matplotlib.pyplot as plt

from pyworld3 import World3
from pyworld3.utils import plot_world_variables

# %%
# Config
back_ground_color = (1.0, 1.0, 1.0, 1.0)  # (1.0, 1.0, 1.0, 0.0)
params = {
    'lines.linewidth': '2',
    'font.size': 18,
    'figure.figsize': (12, 9), # (20, 15), # (16, 9),  # 
    "figure.facecolor": back_ground_color,
    "axes.facecolor":   back_ground_color,
    }
plt.rcParams.update(params)
B_WRITE = False

# %%
world3 = World3()
world3.init_world3_constants()
world3.init_world3_variables()
world3.set_world3_table_functions()
world3.set_world3_delay_functions()
world3.run_world3(fast=False)

# %%
plot_world_variables(world3.time,
                     [world3.nrfr, world3.iopc, world3.fpc, world3.pop,
                      world3.ppolx],
                     ["NRFR",   # nonrenewable resource fraction remaining [].
                      "IOPC",   # industrial output per capita [dollars/person-year].
                      "FPC",    # food per capita [vegetable-equivalent kilograms/person-year].
                      "POP",    # Population
                      "PPOLX"], # index of persistent pollution [].
                     [[0, 1], [0, 1e3], [0, 1e3], [0, 16e9], [0, 32]],
                     # img_background="./img/fig7-7.png",
                     # figsize=(7, 5),
                     title="World3 standard run")
plt.show()
if B_WRITE:
    plt.savefig("fig_world3_standard_a_mod.pdf")

plot_world_variables(world3.time,
                     [world3.fcaor, world3.io, world3.tai, world3.aiph,
                      world3.fioaa],
                     ["FCAOR",   # fraction of capital allocated to obtaining resources [].
                      "IO",      # industrial output [dollars/year].
                      "TAI",     # total agricultural investment [dollars/year].
                      "AI",      # agricultural inputs [dollars/year].
                      "FIOAA"],  # fraction of industrial output allocated to agriculture [].
                     [[0, 1], [0, 4e12], [0, 4e12], [0, 2e2], [0, 0.201]],
                     # img_background="./img/fig7-8.png",
                     # figsize=(7, 5),
                     title="World3 standard run - Capital sector")
plt.show()
if B_WRITE:
    plt.savefig("fig_world3_standard_b_mod.pdf")

plot_world_variables(world3.time,
                     [world3.ly, world3.al, world3.fpc, world3.lmf,
                      world3.pop],
                     ["LY",   # land yield [vegetable-equivalent kilograms/hectare-year].
                      "AL",   # arable land [hectares].
                      "FPC",  # Food per Capita
                      "LMF",  # lifetime multiplier from food [].   
                      "POP"], # Population
                     [[0, 4e3], [0, 4e9], [0, 8e2], [0, 1.6], [0, 16e9]],
                     # img_background="./img/fig7-9.png",
                     # figsize=(7, 5),
                     title="World3 standard run - Agriculture sector")
plt.show()
if B_WRITE:
    plt.savefig("fig_world3_standard_c_mod.pdf")

# %%