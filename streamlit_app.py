import streamlit
streamlit.title('My parents new healthy diner!')

streamlit.header('Breakfast Menu')
streamlit.text('Avocado on soughdough')
streamlit.text('Eggs benedict')
streamlit.text('Full English')

streamlit.header('Build your own smoothie!')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
