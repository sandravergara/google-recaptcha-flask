from flask import Flask, render_template, request

from form import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sands.2019'
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']= '6LfT_6sUAAAAAK-d2bDrchkYHmFIvXT3ZTL0XwUh'
app.config['RECAPTCHA_PRIVATE_KEY']= '6LfT_6sUAAAAAMt-mX2H4RFCY_50AMpL4Iio39Du'
app.config['RECAPTCHA_OPTIONS']= {'theme':'black'}

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return "The form has been submitted. Success"

    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(port=5000, debug=True)