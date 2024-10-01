from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route("/") 
def index():
    return render_template('index.html')

@app.route('/giris', methods=['GET', 'POST']) 

def giris():

    if request.method == 'POST':
        gmail = request.form['gmail']
        kullanici_adi = request.form['kullanici_adi']
        sifre = request.form['sifre']


        return render_template( 'giris.html', gmail=gmail, kullanici_adi=kullanici_adi, sifre=sifre )

    return render_template( 'giris.html')


if __name__ == "__main__":
    app.run(debug=True)
