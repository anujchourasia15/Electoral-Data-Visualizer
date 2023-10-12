import pandas as pd
from sqlalchemy import create_engine

# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your MySQL credentials and database name
db_uri = "mysql+pymysql://myuser:mypassword@db:3306/mydatabase"
engine = create_engine(db_uri)

def data(df,city_name):
    df.drop('Unnamed: 0', axis=1, inplace=True)
    # df.drop('Unnamed: 0.1', axis=1, inplace=True)
    # df.drop('Unnamed: 0.2', axis=1, inplace=True)

    #print(df.head())
    # Replace 'your_table_name' with the desired table name
    table_name = '{}_data'.format(city_name)

    # Write the DataFrame to MySQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)


d_name = {
    154: "GOVINDPURA",
    204: "INDORE"
}

for i in d_name.values():
    city_name = i.lower()
    df = pd.DataFrame(pd.read_excel("./excel/{}_data.xlsx".format(i)))
    print(data(df, city_name))