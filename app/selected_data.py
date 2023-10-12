import base64
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
from io import BytesIO
from matplotlib import pyplot as plt
import mysql.connector as sql_connector
matplotlib.use('Agg')

def get_graph(table_name):
    # Create a database connection
    connection = sql_connector.connect(
        database='mydatabase',
        user='myuser',
        passwd='mypassword',
        host='db',
        port='3306',
        charset='utf8mb4'
    )

    cursor = connection.cursor()
    query = "SELECT * FROM {}_data;".format(table_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])
    cursor.close()
    connection.close()

    for i in df["GENDER"]:
        if(i == "पुरुष"):
            df["GENDER"] = df["GENDER"].replace({"पुरुष": "MALE"})
        elif(i == "महिला"):
            df["GENDER"] = df["GENDER"].replace({"महिला": "FEMALE"})
        else:
            pass

    data = pd.DataFrame({'Gender': df["GENDER"],
                        'Age': df["AGE"]})

    plt.figure(figsize=(8, 6))

    # # 1. Bar Plot
    # plt.subplot(2, 2, 1)
    # plt.grid(linestyle='--')
    # sns.barplot(x='Gender', y='Age', data=data, palette='pastel')
    # plt.title('Bar Plot')
    # plt.tight_layout()
    # plt.grid(True)

    # 3. Box-and-Whisker Plot
    plt.subplot(2, 2, 1)
    sns.boxplot(x='Gender', y='Age', data=data, palette='pastel')
    plt.title('Box-and-Whisker Plot')
    plt.grid(True)
    
    

    # 2. Histogram
    plt.subplot(2, 2, 2)
    sns.histplot(data=data, x='Age', hue='Gender', kde=True)
    plt.title('Histogram')
    plt.grid(True)


    # 5. Kernel Density Plot
    plt.subplot(2, 2, 3)
    sns.kdeplot(data=data, x='Age', hue='Gender', common_norm=False)
    plt.title('Kernel Density Plot')
    plt.grid(True)

    # plt.subplot(2, 2, 3)
    # heatmap_data = data.pivot_table(index='Age', columns='Gender', aggfunc='size', fill_value=0)
    # sns.heatmap(heatmap_data, cmap='YlGnBu')
    # plt.title('Heatmap')
    # plt.grid(True)
    

    # 6. Scatter Plot
    plt.subplot(2, 2, 4)
    sns.scatterplot(data=data, x='Age', y=np.random.randn(len(data)), hue='Gender')
    plt.title('Scatter Plot')
    plt.grid(True)
    

    # # 8. Pie Chart
    # plt.subplot(2, 2, 1)
    # gender_counts = data['Gender'].value_counts()
    # plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    # plt.title('Pie Chart')
    # plt.grid(True)




    # Convert the entire plot to a BytesIO object
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close()

    # Embed the entire plot in the HTML template
    graph = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return graph