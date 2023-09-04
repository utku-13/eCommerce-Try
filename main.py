from flask import Flask, render_template

app = Flask(__name__)

ferrari_pics = ["https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Ferrari_F8_Tributo_Genf_2019_1Y7A5665.jpg/1200px-Ferrari_F8_Tributo_Genf_2019_1Y7A5665.jpg",
                "https://hips.hearstapps.com/hmg-prod/images/roa080120fea-ferrari-5-1598543431.jpg?crop=0.862xw:0.727xh;0,0.168xh&resize=1200:*",
                "https://o.aolcdn.com/images/dims3/GLOB/legacy_thumbnail/1062x597/format/jpg/quality/100/https://s.aolcdn.com/os/ab/_cms/2022/04/05044014/Ferrari-F8-Tributo-front-three-quarter1.jpg"]

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/ferrari')
def ferrari():
    return render_template('ferrari.html')

@app.route('/porsche')
def porsche():
    return render_template('porsche.html')

@app.route('/bmw')
def bmw():
    return render_template('bmw.html')

@app.route("/ferrari/sale")
def saleferrari():
    return render_template('saleferrari.html', ferrari_pics = ferrari_pics)

@app.route('/porsche/sale')
def saleporsche():
    return render_template('saleporsche.html')

@app.route('/bmw/sale')
def salebmw():
    return render_template('salebmw.html')

if __name__ == '__main__':
    app.run(debug=True)