import pandas as pd



def describe(df: pd.DataFrame) -> pd.DataFrame: 
    """
    Função que gera um describe otimizado de um DataFrame do Pandas,
    arredondando as colunas numéricas para duas casas decimais.

    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        DataFrame: DataFrame com o describe com as colunas numéricas arredondadas.
    """

    desc_df = df.describe() 

    desc_df = desc_df.round(2) 

    return desc_df 



def inspect_outliers(df: pd.DataFrame, column: str, whisker_width: float = 1.5) -> pd.DataFrame: 
    """
    Função que identifica e retorna as linhas de um DataFrame Pandas que contêm
    outliers em uma coluna, com base na regra do IQR (Interquartile Range).

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        column (str): Nome da coluna a ser inspecionada.
        whisker_width (float, opcional): Largura do "bigode" (multiplicador do IQR) 
            usada para definir os limites inferior e superior. Padrão = 1.5.

    Returns:
        DataFrame: DataFrame apenas com os outliers inferiores e superiores.
    """

    q1 = df[column].quantile(0.25) 

    q3 = df[column].quantile(0.75) 

    iqr = q3 - q1 

    lower_bound = q1 - whisker_width * iqr 

    upper_bound = q3 + whisker_width * iqr 

    outliers_df = df[(df[column] < lower_bound) | (df[column] > upper_bound)] 

    return outliers_df 



def groupby_count(df: pd.DataFrame, column: str, ascending: bool = True) -> pd.DataFrame: 
    """
    Função para agrupar um DataFrame Pandas por uma coluna e retorna
      as contagens percentuais e absolutas.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        column (str): Nome da coluna para agrupamento.
        ascending (bool, opcional): Define se o resultado deve ser ordenado em ordem crescente. Padrão = True.

    Returns:
        DataFrame: DataFrame com o agrupamento da coluna segmentado por percentual e contagem.
    """

    result = ( 
        
        df.groupby(column, observed = True)

            .size() 

            .reset_index(name = 'Count') 

            .assign(Percentage  = lambda d: ((d['Count'] / d['Count'].sum()) * 100).round(1))

            .sort_values(column, ascending = ascending) 

            [[column, 'Percentage', 'Count']] 

    )

    return result