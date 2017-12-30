from IPython.display import display


def print_df(df):
	display(df.head())


def print_dfs(df_list):
	for df in df_list:
		print_df(df)
