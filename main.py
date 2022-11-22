# Import Python modules
import json
from typing import Union
import pandas as pd


def set_df_schema():
    """
    It returns a dictionary with the column names and their datatypes
    to be used in the creation of the dataframe.

    Args:
        None.
    Returns:
        dtype_cols_dict (dict): a dictionary with the columns and their types.
    """

    # Set DICT with column names and their datatypes.
    dtype_cols_dict = {
    'assessment_id': pd.Int64Dtype(),
    'patient_id': pd.Int64Dtype(),
    'event_id': pd.Int64Dtype(),
    'institution': pd.Int64Dtype(),
    'birthdate': 'datetime64',
    'completed_at': 'datetime64',
    'created_at': 'datetime64',
    'updated_at': 'datetime64',
    'event_date': 'datetime64',
    'answers': str,
    'disease': str,
    'sex': str,
    'timing' : str,
    'laterality': str,
    'event': str
    }
    return dtype_cols_dict


def create_df_from_csv(input_file:str):
    """
    It reads a CSV file and returns a Pandas dataframe.

    Args:
        input_file (str): the path to the CSV input file.

    Returns:
        df (pd.Dataframe): a dataframe with the columns specified in the 'set_df_schema' function.
    """

    # Create a DF from the CSV file.
    df = pd.read_csv(input_file, usecols=list(set_df_schema().keys()))
    return df


def filter_df(df:pd.DataFrame, filter_date:str):
    """
    It takes a dataframe as input, filters it, and returns a filtered dataframe.

    Args:
        df (pd.Dataframe): the dataframe to be filtered.
        filter_date (str): the date to filter the dataframe.

    Returns:
        df (pd.Dataframe): a dataframe with the filtered data.
    """

    # Apply filters "notna" and "Cataract" to the DF.
    df = df.query('completed_at.notna() & (disease == "Cataract")')
    # Apply date filter to the DF.
    df = df.query("event_date > @filter_date").reset_index(drop=True)
    return df


def change_df_dtype(df:pd.DataFrame):
    """
    For each column in the dataframe, if the column is not null,
    then convert the column to the appropriate datatype.

    Args:
        df (pd.DataFrame): the dataframe to be processed.

    Returns:
        df (pd.DataFrame): a dataframe with the datatypes of the columns changed.
    """

    # Set the datatype of the columns.
    for col, dtype in set_df_schema().items():
        f = df[col].notna()
        if dtype == 'datetime64':
            df.loc[f, col] = pd.to_datetime(df[col], errors="coerce")
        else:
            df.loc[f, col] = df[col].astype(dtype)
    return df


def make_df_answer(df:pd.DataFrame):
    """
    Takes a dataframe with a column named 'answers' that contains a list of dictionaries,
    and returns a dataframe with the dictionaries as rows.

    Args:
        df (pd.DataFrame): the dataframe you want to convert.

    Returns:
        df (pd.DataFrame): a dataframe with the values.
    """

    # Convert the column 'answers' to a list of dictionaries.
    df['answers'] = df['answers'].apply(
      lambda val: json.loads(val)
      if isinstance(val, str)
      else val
    )

	# Assure that all values are dict types.
    assert df['answers'].apply(type).eq(dict).all()
    # Transform the json that is in each cell of the 'answers' column into a dataframe.
    df = pd.json_normalize(df['answers'])
    # Set dataframe header to lower case.
    df.columns = df.columns.str.lower()
    return df


def value_choice_extractor(dictionary:dict):
    """
    If the dictionary has a key called 'value', return the value of that key.
    If the dictionary has a key called 'choice', return the value of that key.
    If neither of those keys exist, return 'pd.NA'.

    Args:
        dictionary (dict): the dictionary you want to extract the value from.

    Returns:
        The value of the key 'value', the value of the key 'choice' or 'pd.NA'.
    """
    # Execute different procedures based on the conditions.
    for key in dictionary.keys():
        if key == 'value':
            return dictionary['value']
        if key == 'choice':
            return dictionary['choice']
        return pd.NA


def extract_choices(answer: Union[list, dict]):
    """
    If the answer it's not a list, then return itself.
    If the list is empty, return 'pd.NA'.
    If the list has only one element, return the value from the dictionary.
    If the list has more than one element, return a comma separated string of the values
    from the dictionaries.

    Args:
        answer (Union[list, dict]): the list/dict that you want to extract the values from.

    Returns:
        The value of the key 'value', the value of the key 'choice' or 'pd.NA'.
    """

    # Execute different procedures based on the conditions.
    if not isinstance(answer, list):
        return answer
    if len(answer) == 0:
        return pd.NA
    if len(answer) == 1:
        return value_choice_extractor(answer[0])
    return ', '.join([str(value_choice_extractor(dictionary)) for dictionary in answer])


def apply_df_answer(df_answer:pd.DataFrame):
    """
    It takes a dataframe, applies a function to each cell, and returns the result.

    Args:
        df_answer (pd.DataFrame): the dataframe that you want to apply the function to.

    Returns:
        df_answer (pd.DataFrame): a dataframe.
    """

    # Apply the function 'extract_choices'.
    df_answer = df_answer.applymap(extract_choices)
    # Remove all columns that are completely empty.
    df_answer = df_answer.dropna(axis=1, how='all')
    return df_answer


def prep_df(df:pd.DataFrame, df_answer:pd.DataFrame):
    """
    It takes two dataframes: removes the 'answers' column from the first
    dataframe, and joins the two DFs.

        Args:
        df (pd.DataFrame): the original dataframe.
        df_answer (pd.DataFrame): the second dataframe.

    Returns:
        df (pd.DataFrame): a dataframe with the 'answers' column removed and the
        'df_answer' dataframe joined to it.

    """

    # Remove the 'answers' column from the DF.
    df = df.drop("answers", axis=1)
    # Join the two dataframes.
    df = df.join(df_answer)
    return df


def save_output_file(output_file:str, df:pd.DataFrame):
    """
    It takes a dataframe and saves it as a CSV file.

    Args:
        output_file (str): The name of the CSV output file.
        df (pd.DataFrame): the dataframe you want to save.

    Returns:
        None.
    """

    # Create CSV file from dataframe.
    df.to_csv(output_file)


def main(input_file:str, output_file:str, filter_date:str):
    """
    Reads a csv file, filters it by a date, changes the data types,
    creates a new dataframe from the column 'answers' and extracts the values from it,
    join the new dataframe to the original one,
    and saves the final dataframe as the output file.

    Args:
        input_file (str): the name of the CSV input file.
        output_file (str): the name of the CSV output file.
        filter_date (str): the date you want to filter the dataframe by.

    Returns:
        None.
    """
    # Set the order of execution and call the functions with the appropriate arguments.
    df = create_df_from_csv(input_file)
    df = filter_df(df, filter_date)
    df = change_df_dtype(df)
    df_series = make_df_answer(df)
    df_aux = apply_df_answer(df_series)
    df = prep_df(df, df_aux)
    save_output_file(output_file, df)


# Run the main function.
if __name__ == '__main__':
    main(
        r"source_data.csv",
        r"processed_data.csv",
        "2019-06-01"
    )
