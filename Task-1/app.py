from flask import Flask,request 
from flask import jsonify
from flaskext.mysql import MySQL
from datetime import date,timedelta

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'sage'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sage'
app.config['MYSQL_DATABASE_DB'] = 'transaction'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

@app.route('/')
def hello():
    return 'Hello! Welcome to Sage \n'

@app.route('/api/v1/transactions',methods=['GET'])
def transactions():

    input_days = request.args.get('days')
    fromdate = (date.today()-timedelta(days=int(input_days)))
    query="select * from transaction where Date between '{fd} 00:00:00' and '{td} 23:59:59'".format(fd=str(fromdate),td=str(date.today()))
  
    if 'cardtype' in request.args:
        query = query + " and CardType='{ct}'".format(ct=request.args['cardtype'])
    if 'countryorigin' in  request.args:
        query = query + " and CountryOrigin='{co}'".format(co=request.args['countryorigin'])
    if ('fromamount' in request.args and 'toamount' in request.args):
        query = query + " and Amount >='{fa}' and Amount <='{ta}'".format(fa=request.args['fromamount'],ta=request.args['toamount'])

    print(query)
    cursor = mysql.connect().cursor()
    cursor.execute(query)
    results=cursor.fetchall()
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
