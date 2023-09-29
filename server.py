from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)                                                 # create the app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sensors.db"        # configure the SQLite database
db = SQLAlchemy()                                                     # create the extension
db.init_app(app)                                                      # initialize the app with the extension

class sensordata(db.Model):                                           # make schema for table creation
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), unique=True, nullable=False)
    temp = db.Column(db.Integer)
    pres = db.Column(db.Integer)
    hum = db.Column(db.Integer)

with app.app_context():                                               # create table 
    db.create_all()

city= ["Mumbai", "Chennai", "Kochi"]                                  # Initial dummy data 
temp = [35,36,34]
pres= [100,101,102]
hum= [51,49,50]

with app.app_context():                                               # Add initial data in database
    try:
        for i in range(3):
            data = sensordata( city=city[i], temp=temp[i], pres=pres[i], hum=hum[i])
            db.session.add(data)
            db.session.commit()
    except:
        pass


@app.route("/")                                                       # Home route 
def home():    
    all_data = db.session.execute(db.select(sensordata)).scalars()
    return render_template("index.html", all_data=all_data)


@app.route("/add", methods=["GET","POST"])                            # Add route
def add():
    if request.method == "POST":
        try:
                                                                      # Create Record
            if request.form["entered_city"]:
                
                new_data = sensordata(
                    city=request.form["entered_city"].title(),
                    temp=request.form["entered_temp"],
                    pres=request.form["entered_pres"],
                    hum=request.form["entered_hum"])
                
                db.session.add(new_data)
                db.session.commit()
            pass
        except:
            pass
        finally:            
            return redirect(url_for('home'))
        
    return render_template("add.html")



@app.route("/update", methods=["GET", "POST"])                        # Update route
def update():
    if request.method == "POST":
        try:
                                                                      # Update record
            pass
        except:
            pass        
        finally:
            return redirect(url_for("home"))
    
    return render_template("update.html")


@app.route("/sort", methods=["POST"])                                 # Sort route
def sort():
    try:
        pass
    except:
        pass

    finally:
        return redirect(url_for("home") )

   

@app.route("/filter", methods=["POST"])                               # Filter route
def filter(): 
    return redirect(url_for("home"))




if __name__=='__main__':
    app.run(debug=True)