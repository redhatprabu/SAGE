import yaml
import random
import argparse
from faker import Faker
import mysql.connector



def data():

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", help="No of Transactions", dest="limit")
    options = parser.parse_args()

    if options.limit is None:
        print("Enter Number of Trasaction to be added by passing --limit as arguement")
        exit()

    with open("config.yml", 'r') as config_file:
        config = yaml.load(config_file)

    db = mysql.connector.connect ( host = config['mysql']['host'],
                                   user = config['mysql']['user'],
                                   passwd = config['mysql']['password'],
                                   database = config['mysql']['database'] 
                                  )

    cursor=db.cursor()
          

    fake = Faker()
    row = 0
    for i in range(int(options.limit)):
        add_employee = ("INSERT INTO employees "
               "(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")
                
        query = ("Insert into transaction(Date,Currency,Amount,Vendor,CardType,"
                 "CardNumber,Address,CountryOrigin)" 
                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
        data =  (str(fake.date_time_this_decade()),fake.currency()[0],
                 round(random.uniform(1, 250000), 2),fake.company(),
                 fake.credit_card_provider(),fake.credit_card_number(),
                 fake.address(),fake.country())
        cursor.execute(query,data)        
        db.commit()
        row += cursor.rowcount
        
    print("{records} record inserted.".format(records=row))

if __name__ == "__main__":
    data()
