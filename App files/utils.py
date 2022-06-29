import numpy as np
from pandas.api.types import is_numeric_dtype
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sb


def nan_replace(tabel):
    assert isinstance(tabel, DataFrame)
    nume_variabile = list(tabel.columns)
    for v in nume_variabile:
        if any(tabel[v].isna()):
            if is_numeric_dtype(tabel[v]):
                tabel[v].fillna(tabel[v].mean(), inplace=True)
            else:
                tabel[v].fillna(tabel[v].mode()[0], inplace=True)
    return tabel


def getDataFrame(x, nume_linii=None, nume_coloane=None):
    t = DataFrame(x, nume_linii, nume_coloane)
    return t


def corelograma(t, vmin=-1, vmax=1, titlu="Corelatii factoriale"):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax_ = sb.heatmap(t, vmin=vmin, vmax=vmax, cmap="RdYlBu", annot=True, ax=ax)
    ax_.set_xticklabels(t.columns, rotation=30, ha="right")
    # plt.show()


def plot_corelatii(t, var_x, var_y, titlu="Plot corelatii", aspect="auto"):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var_x, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var_y, fontdict={"fontsize": 12, "color": "b"})

    ax.set_aspect(aspect)

    theta = np.arange(0, 2 * np.pi, 0.01)

    ax.plot(np.cos(theta), np.sin(theta), color="b")

    ax.axhline(0)
    ax.axvline(0)

    ax.scatter(t[var_x], t[var_y], c="r")
    for i in range(len(t)):
        ax.text(t[var_x].iloc[i], t[var_y].iloc[i], t.index[i])
    # plt.show()


def plot_componente(t, var_x, var_y, titlu="Plot componente", aspect="auto"):
    fig = plt.figure(figsize=(15, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var_x, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var_y, fontdict={"fontsize": 12, "color": "b"})

    ax.set_aspect(aspect)

    ax.scatter(t[var_x], t[var_y], c="r")
    for i in range(len(t)):
        ax.text(t[var_x].iloc[i], t[var_y].iloc[i], t.index[i])
    # plt.show()


def show():
    plt.show()
