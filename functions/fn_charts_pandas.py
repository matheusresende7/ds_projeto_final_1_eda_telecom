import math
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.cm import ScalarMappable
from matplotlib.colors import CenteredNorm, ListedColormap
from typing import List



os.environ['OMP_NUM_THREADS'] = '9'



def countplot(df: pd.DataFrame, x_columns: List[str], num_cols: int = 3, height_figsize: int = 5) -> tuple[plt.Figure, list]:
    """
    Função que gera uma lista de gráficos de contagem.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        x_columns (List[str]): Lista de colunas para o eixo X para criação dos gráficos de contagem.
        num_cols (int, opcional): Número de gráficos de contagem por linha. Padrão = 3.
        height_figsize (int, opcional): Altura da figura. Padrão = 5.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    total_columns = len(x_columns)

    num_rows = math.ceil(total_columns / num_cols)

    fig, axs = plt.subplots(figsize = (20, height_figsize * num_rows), nrows = num_rows, ncols = num_cols, tight_layout = True)

    axs = axs.flatten()

    for i, x_column in enumerate(x_columns):

        order = sorted(df[x_column].dropna().unique(), reverse = False)

        sns.countplot(data = df, x = x_column, ax = axs[i], order = order)

        axs[i].set(title = f'Barplot - {x_column}', xlabel = '', ylabel = '')

    for ax in axs[total_columns:]:

        ax.axis('off')

    return fig, axs



def scatterplot(df: pd.DataFrame, x_columns: List[str], y_column: str, hue_column: str = None, num_cols: int = 3, height_figsize: int = 5) -> tuple[plt.Figure, list]:
    """
    Função que gera uma lista de gráficos de dispersão.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        x_columns (List[str]): Lista de colunas para o eixo X para criação dos gráficos de dispersão.
        y_column (str): Coluna para o eixo Y com alta cardinalidade, amplitude e escala contínua.
        hue_column (str, opcional): Coluna "categórica" usada como hue. Padrão = None.
        num_cols (int, opcional): Número de gráficos de dispersão por linha. Padrão = 3.
        height_figsize (int, opcional): Altura da figura. Padrão = 5.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    total_columns = len(x_columns)

    num_rows = math.ceil(total_columns / num_cols)

    fig, axs = plt.subplots(figsize = (20, height_figsize * num_rows), nrows = num_rows, ncols = num_cols, tight_layout = True)

    axs = axs.flatten()

    for i, x_column in enumerate(x_columns):

        sns.scatterplot(data = df, x = x_column, y = y_column, hue = hue_column, ax = axs[i], palette = 'tab10' if hue_column else None)

        axs[i].set(title = f'Scatterplot - {y_column} vs {x_column}', xlabel = '', ylabel = '')

    for ax in axs[total_columns:]:

        ax.axis('off')

    return fig, axs



def histplot(df: pd.DataFrame, x_columns: List[str], hue_column: str = None, num_cols: int = 3, height_figsize: int = 5, alpha: float = 0.5, kde: bool = False) -> tuple[plt.Figure, list]:
    """
    Função que gera uma lista de histogramas.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        x_columns (List[str]): Lista de colunas para o eixo X para criação dos histogramas.
        hue_column (str, opcional): Coluna "categórica" usada como hue. Padrão = None.
        num_cols (int, opcional): Número de histogramas por linha. Padrão = 3.
        height_figsize (int, opcional): Altura da figura. Padrão = 5.
        alpha (float, opcional): Transparência dos histogramas. Padrão = 0.5.
        kde (bool, opcional): Exibição da linha KDE. Padrão = True.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    total_columns = len(x_columns)

    num_rows = math.ceil(total_columns / num_cols)

    fig, axs = plt.subplots(figsize = (20, height_figsize * num_rows), nrows = num_rows, ncols = num_cols, tight_layout = True)

    axs = axs.flatten()

    for i, x_column in enumerate(x_columns):

        sns.histplot(data = df, x = x_column, hue = hue_column, ax = axs[i], kde = kde, alpha = alpha, palette = 'tab10' if hue_column else None)

        axs[i].set(title = f'Histplot - {x_column}', xlabel = '', ylabel = '')

    for ax in axs[total_columns:]:

        ax.axis('off')

    return fig, axs



def boxplot(df: pd.DataFrame, y_columns: List[str], x_column: str = None, hue_column: str = None, num_cols: int = 3, height_figsize: int = 5) -> tuple[plt.Figure, list]:
    """
    Função que gera uma lista de diagramas de caixa.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        y_columns (List[str]): Lista de colunas para o eixo Y para criação dos diagramas de caixa.
        x_column (str): Coluna para o eixo X. Padrão = None.
        hue_column (str, opcional): Coluna "categórica" usada como hue. Padrão = None.
        num_cols (int, opcional): Número de diagramas de caixa por linha. Padrão = 3.
        height_figsize (int, opcional): Altura da figura. Padrão = 5.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    total_columns = len(y_columns)

    num_rows = math.ceil(total_columns / num_cols)

    fig, axs = plt.subplots(figsize = (20, height_figsize * num_rows), nrows = num_rows, ncols = num_cols, tight_layout = True)

    axs = axs.flatten()

    for i, y_column in enumerate(y_columns):

        sns.boxplot(data = df, x = x_column, y = y_column, hue = hue_column, ax = axs[i], showmeans = True, palette = 'tab10' if hue_column else None)

        axs[i].set(title = f'Boxplot - {y_column}', xlabel = '', ylabel = '')

    for ax in axs[total_columns:]:

        ax.axis('off')

    return fig, axs



def heatmap(df: pd.DataFrame) -> tuple[plt.Figure, list]:
    """
    Função que gera um mapa de calor.

    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    fig, axs = plt.subplots(figsize = (7.5, 7.5), nrows = 1, ncols = 1, tight_layout = True)

    sns.heatmap(data = df, annot = True, ax = axs, fmt = '.1f', cmap = 'coolwarm_r', annot_kws = {'size': 6})

    axs.set_title('Heatmap', fontsize = 10); axs.set_xticklabels(axs.get_xticklabels(), fontsize = 6); axs.set_yticklabels(axs.get_yticklabels(), fontsize = 6)

    axs.collections[0].colorbar.ax.tick_params(labelsize = 6)

    return fig, axs



def barplot(df: pd.DataFrame, x_column: str, y_column: str, num_cols: int = 3, height_figsize: int = 5) -> tuple[plt.Figure, list]:
    """
    Função que gera uma lista de gráficos de barras.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        x_columns (List[str]): Lista de colunas para o eixo X para criação dos gráficos de barras.
        y_column (str): Coluna para o eixo Y.
        num_cols (int, opcional): Número de diagramas de caixa por linha. Padrão = 3.
        height_figsize (int, opcional): Altura da figura. Padrão = 5.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    total_columns = len([x_column])

    num_rows = math.ceil(total_columns / num_cols)

    fig, axs = plt.subplots(figsize = (20, height_figsize * num_rows), nrows = num_rows, ncols = num_cols, tight_layout = True)

    axs = axs.flatten()

    order = sorted(df[x_column].dropna().unique(), reverse = False)

    sns.barplot(data = df, x = x_column, y = y_column, ax = axs[0], order = order)

    for bar in axs[0].patches:

        height = bar.get_height()

        axs[0].annotate(f'{height:.0f}', xy = (bar.get_x() + bar.get_width() / 2, height), ha = 'center', va = 'bottom')

    axs[0].set(title = f'Barplot - {x_column}', xlabel = '', ylabel = '', yticks = [])
    
    for ax in axs[total_columns:]:

        ax.axis('off')

    return fig, axs



def barplot_donutplot(df: pd.DataFrame, x_column: List[str], y_column: str) -> tuple[plt.Figure, list]:
    """
    Função que gera uma lista de gráficos de barras.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        x_column (List[str]): Lista de colunas para o eixo X para criação dos gráficos de barras.
        y_column (str): Coluna para o eixo Y.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    fig, axs = plt.subplots(figsize = (20, 5), nrows = 1, ncols = 2, tight_layout = True)

    order = sorted(df[x_column].dropna().unique(), reverse = False)

    sns.barplot(data = df, x = x_column, y = y_column, ax = axs[0], order = order)

    axs[0].set(title = f'Barplot - {x_column}', xlabel = '', ylabel = '', yticks = [])

    for bar in axs[0].patches:

        height = bar.get_height()

        axs[0].annotate(f'{height:.0f}', xy = (bar.get_x() + bar.get_width() / 2, height), ha = 'center', va = 'bottom')

    wedges, texts, autotexts = axs[1].pie(
        df[y_column],
        labels = df[x_column],
        autopct = lambda pct: f'{pct:.1f}%',
        pctdistance = 0.775, 
        startangle = 90,
        counterclock = False,
        radius = 1,
        wedgeprops = dict(width = 0.4, edgecolor = 'white', linewidth = 2),
        textprops = dict(color = 'w')
    )

    axs[1].set(title = f'Donutplot - {x_column}', frame_on = True, aspect = 'equal', xlim = (-2.55, 2.55), ylim = (-1.10, 1.10))

    axs[1].legend(wedges, df[x_column], title = x_column, bbox_to_anchor = (0.95, 0.9))

    for i in texts:

        i.set_visible(False)

    for i in autotexts:

        i.set(fontsize = 12, weight = 'bold')

    return fig, axs



def barplot_correlation(df: pd.DataFrame, y_column: str, y_column_max: float, title: str = None) -> tuple[plt.Figure, list]:
    """
    Função que gera um gráfico de barra.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        y_column (str): Coluna usada como eixo Y.
        y_column_max (float): Valor máximo do eixo Y do gráfico.
        title (str, opcional): Título do gráfico. Padrão = None.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    smap = ScalarMappable(norm = CenteredNorm(vcenter = 0, halfrange = y_column_max), cmap = 'coolwarm_r')

    listed_colors = ListedColormap([smap.to_rgba(x) for x in y_column]).colors
    
    fig, axs = plt.subplots(figsize = (14,4), nrows = 1, ncols = 1)

    sns.barplot(x = df.index, y = y_column, hue = df.index, palette = listed_colors, legend = False)

    axs.set(title = f'Barplot - {title}', xlabel = '', ylabel = 'Correlation')

    axs.tick_params(axis = 'x', rotation = 90)

    return fig, axs



def scatterplot_clusters_2D(df: pd.DataFrame, columns: list[str], clusters: int, centroids: list, show_centroids: bool = True, show_points: bool = True, column_clusters: str = None) -> tuple[plt.Figure, list]:
    """
    Função que gera um gráfico 2D dos clusters após redução PCA.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        columns (list[str]): Lista contendo as colunas.
        clusters (int): Número de clusters.
        centroids (list): Lista com as coordenadas dos centróides.
        show_centroids (bool, opcional): Exibição dos centróides. Padrão = True.
        show_points (bool, opcional): Exibição dos pontos. Padrão = True.
        column_clusters (str, opcional): Coluna com os clusters. Padrão = None.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    fig, axs = plt.subplots(figsize = (7, 5), nrows = 1, ncols = 1)
    
    colors = ListedColormap(plt.cm.tab10.colors[:clusters])

    for i, centroid in enumerate(centroids):

        if show_centroids:

            axs.scatter(*centroid, s = 500, alpha = 0.5)

            axs.text(*centroid, f'{i}', fontsize = 20, horizontalalignment = 'center', verticalalignment = 'center')

        if show_points:

            axs.scatter(x = df[columns[0]], y = df[columns[1]], c = column_clusters, cmap = colors)

            axs.legend(*axs.collections[-1].legend_elements(), bbox_to_anchor = (1.3, 1))

    axs.set(title = 'Clusters', xlabel = columns[0], ylabel = columns[1])

    return fig, axs



def lineplot_elbow_silhouette(elbow: dict, silhouette: list, k_values: list) -> tuple[plt.Figure, list]:
    """
    Função que gera os gráficos do método do cotovelo e do método da silhueta.

    Args:
        elbow (dict): Dicionário com as inércias para cada valor de k.
        silhouette (list): Lista com os valores do coeficiente da silhueta para cada valor de k.
        k_values (list): Lista com o intervalo inicial e final (não inclusivo) 
            do número de clusters a serem testados.

    Returns:
        tuple: Uma tupla contendo a figura (`fig`) e a lista de eixos (`axs`) gerados.
    """

    fig, axs = plt.subplots(figsize = (15, 5), nrows = 1, ncols = 2, tight_layout = True)

    sns.lineplot(x = list(elbow.keys()), y = list(elbow.values()), ax = axs[0], marker = 'o')

    axs[0].set(title = 'Elbow Method', xlabel = 'k values', ylabel = 'Inertia')

    axs[0].fill_between(list(elbow.keys()), list(elbow.values()), y2 = min(elbow.values()), color = 'lightgrey', alpha = 0.3)

    sns.lineplot(x = list(k_values), y = silhouette, ax = axs[1], marker = 'o')

    axs[1].set(title = 'Silhouette Method', xlabel = 'k values', ylabel = 'Silhouette Score')

    axs[1].fill_between(list(list(k_values)), list(silhouette), y2 = min(silhouette), color = 'lightgrey', alpha = 0.3)

    return fig, axs