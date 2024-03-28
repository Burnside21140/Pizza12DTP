from flask import Flask, render_template

import sqlite3


app = Flask(__name__)


@app.route("/")  # ROUTE DECORATOR
def home():     # ROUTE FUNCTION
    return render_template("home.html")


@app.route("/pizza/<string:pizza_id>")
def pizza(pizza_id):
    connection = sqlite3.connect('pizzas.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Pizza where id = ?", (pizza_id,))
    pizza = cursor.fetchone()
    connection.close()
    return render_template('pizza.html', pizzaname=pizza[1], pizzadesc=pizza[2], pizzaimg=pizza[4])


@app.route("/pizzas")
def pizzas():
    connection = sqlite3.connect('pizzas.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Pizza")
    pizzas = cursor.fetchall()
    print("Pizzas:", pizzas)
    connection.close()
    pizzalist = []
    for i in pizzas:
        print("i:", i)
        item = [i[0], i[1]]
        pizzalist.append(item)
    print(pizzalist)
    return render_template('pizzas.html', pizzas=pizzalist)


if __name__ == "__main__":
    app.run(debug=True)  # live updates code when building a website
