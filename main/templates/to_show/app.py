import streamlit as st
from pathlib import Path
import mysql.connector as mysql
import pandas as pd
import plotly.graph_objs as go

BASE_DIR = Path(__file__).resolve().parent.parent

connection = mysql.connect(
    host='localhost',
    user='root',
    password='BigGucciSosa300',
    database='erp215'
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """


def get_data(article_id, start_date, end_date):
    cursor = connection.cursor()
    query = "SELECT stock_quantity, stock_date FROM main_plot WHERE prod_id = %s AND stock_date BETWEEN %s AND %s"
    cursor.execute(query, (article_id, start_date, end_date))

    results = cursor.fetchall()
    data = pd.DataFrame(results, columns=['stock_quantity', 'date'])
    data['date'] = pd.to_datetime(data['date'])
    data = data.set_index('date')
    return data


def get_label(article_id):
    cursor = connection.cursor()
    query = f"SELECT prod_name FROM main_articles WHERE prod_id = {article_id}"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def app():
    with open(BASE_DIR.parent / "templates/to_show/base_streamlit.html") as f:
        base_html = f.read()

    st.set_page_config(page_title="Divalto Connect - Plot", layout="wide")
    st.write(base_html, unsafe_allow_html=True)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    st.title("Plotting stock quantity over time")
    article_id = st.number_input("Enter article ID", min_value=1, step=1)
    start_date = st.date_input("Enter start date")
    end_date = st.date_input("Enter end date")
    if start_date >= end_date:
        st.warning("End date must be after start date")
        return
    data = get_data(article_id, start_date, end_date)
    if data.empty:
        st.warning("No data found for selected article ID and date range")
        return
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['stock_quantity'], mode='lines+markers'))
    fig.update_layout(title=f"Stock quantity for article {article_id} from {start_date} to {end_date}",
                      xaxis_title="Date",
                      yaxis_title="Stock quantity")
    st.plotly_chart(fig, height=5000, width=5000)


if __name__ == '__main__':
    app()

