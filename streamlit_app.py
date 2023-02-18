import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#streamlit.header("Fruityvice Fruit Advice!")
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# #import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


# # gets fruits watermelons details
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # Displays a table
# streamlit.dataframe(fruityvice_normalized)

#xxxxxxxxxxxxxxxxxxxxxxxx
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get Information.")
#   else:
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe(fruityvice_normalized)

# except URLError as e:
#   streamlit.error()

# streamlit.stop()
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get Information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

#import snowflake.connector
# Error source
print(streamlit.secrets)
print(streamlit.secrets["snowflake"])
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if add_my_fruit:
  streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
