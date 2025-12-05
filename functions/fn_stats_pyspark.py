from pyspark.sql import DataFrame
from pyspark.sql.functions import *



def describe(df: DataFrame) -> DataFrame:
    """
    Função que gera um describe otimizado de um DataFrame do PySpark,
    arredondando as colunas numéricas para duas casas decimais.

    Args:
        df (DataFrame): DataFrame de entrada.

    Returns:
        DataFrame: DataFrame com o describe com as colunas numéricas arredondadas.
    """
    
    desc_df = df.describe() 

    numeric_cols = [c for c, t in df.dtypes if t in ('int', 'double', 'float', 'bigint')] 

    for i in numeric_cols: 

        desc_df = desc_df.withColumn(i, round(col(i).cast('double'), 2)) 

    return desc_df 



def summary(df: DataFrame) -> DataFrame:
    """
    Função que gera um summary otimizado de um DataFrame do PySpark,
    arredondando as colunas numéricas para duas casas decimais.

    Args:
        df (DataFrame): DataFrame de entrada.

    Returns:
        DataFrame: DataFrame com o summary com as colunas numéricas arredondadas.
    """

    sum_df = df.summary() 

    numeric_cols = [c for c, t in df.dtypes if t in ('int', 'double', 'float', 'bigint')] 

    for i in numeric_cols: 

        sum_df = sum_df.withColumn(i, round(col(i).cast('double'), 2)) 

    return sum_df 



def inspect_outliers(df: DataFrame, column: str, whisker_width: float = 1.5) -> DataFrame: 
    """
    Função que identifica e retorna as linhas de um DataFrame PySpark que contêm
    outliers em uma coluna, com base na regra do IQR (Interquartile Range).

    Args:
        df (DataFrame): DataFrame de entrada.
        column (str): Nome da coluna a ser inspecionada.
        whisker_width (float, opcional): Largura do "bigode" (multiplicador do IQR) 
            usada para definir os limites inferior e superior. Padrão = 1.5.

    Returns:
        DataFrame: DataFrame apenas com os outliers inferiores e superiores.
    """

    q1 = df.approxQuantile(column, [0.25], 0.01)[0] 

    q3 = df.approxQuantile(column, [0.75], 0.01)[0] 

    iqr = q3 - q1 

    lower_bound = q1 - whisker_width * iqr 

    upper_bound = q3 + whisker_width * iqr 

    outliers_df = df.filter((col(column) < lower_bound) | (col(column) > upper_bound)) 
 
    return outliers_df 



def groupby_count(df: DataFrame, column: str, ascending: bool = True) -> DataFrame: 
    """
    Função para agrupar um DataFrame PySpark por uma coluna e retorna
      as contagens percentuais e absolutas.

    Args:
        df (DataFrame): DataFrame de entrada.
        column (str): Nome da coluna para agrupamento.
        ascending (bool, opcional): Define se o resultado deve ser ordenado em ordem crescente. Padrão = True.

    Returns:
        DataFrame: DataFrame com o agrupamento da coluna segmentado por percentual e contagem.
    """

    result = ( 
        
        df.groupBy(column) 

          .agg(count('*').alias('Count')) 

          .withColumn('Percentage', round((col('Count') / lit(df.count())) * 100, 1)) 
                    
          .orderBy(col(column).asc() if ascending else col(column).desc()) 
          
          .select([column, 'Percentage', 'Count'])  
    
    )

    return result 