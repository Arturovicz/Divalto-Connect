import streamlit as st
from pathlib import Path
import mysql.connector as mysql
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')


BASE_DIR = Path(__file__).resolve().parent.parent

connection = mysql.connect(
    host='localhost',
    user='root',
    password='BigGucciSosa300',
    database='erp215'
)


def get_data(article_id, start_date, end_date):
    cursor = connection.cursor()
    query = "SELECT stock_quantity, date FROM main_plot WHERE article_id = %s AND date BETWEEN %s AND %s"
    cursor.execute(query, (article_id, start_date, end_date))
    results = cursor.fetchall()
    data = pd.DataFrame(results, columns=['stock_quantity', 'date'])
    data['date'] = pd.to_datetime(data['date'])
    data = data.set_index('date')
    return data


def app():
    with open(BASE_DIR.parent / 'templates/to_show/base.html') as f:
        base_html = f.read()

    st.write(base_html, unsafe_allow_html=True)
    st.title("Plotting stock quantity over time")
    article_id = st.number_input("Enter article ID", min_value=1, step=1)
    start_date = st.date_input("Enter start date")
    end_date = st.date_input("Enter end date")
    if start_date >= end_date:
        st.error("End date must be after start date")
        return
    data = get_data(article_id, start_date, end_date)
    if data.empty:
        st.error("No data found for selected article ID and date range")
        return
    plt.figure(figsize=(15, 10))
    plt.plot(data['stock_quantity'])
    plt.xlabel("Date")
    plt.ylabel("Stock quantity")
    plt.title(f"Stock quantity for article {article_id} from {start_date} to {end_date}")
    st.pyplot(plt.gcf())


if __name__ == '__main__':
    app()



