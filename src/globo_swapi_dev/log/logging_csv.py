def set_sent(df, column, index, yes_no):
    df.at[index, column] = yes_no
