from flask import Flask,request,render_template
from convert import *
app = Flask(__name__)
 
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html',result = '  ')
    else:
        system1 = request.form.get('system1')
        system2 = request.form.get('system2')
        number  = request.form.get('number').upper()
          
        if system1 == 'Binary':
            for digit in number:
                    try:
                        digit = int(digit)
                        if not(digit in binary):
                            return render_template('home.html',result = 'Invalid Binary number')
                    except:
                        return render_template('home.html',result = 'Invalid Binary number')

        if system1 == 'Octal':
            for digit in number:
                    try:
                        digit = int(digit)
                        if not(digit in octal):
                            return render_template('home.html',result = 'Invalid Octal number')
                    except:
                        return render_template('home.html',result = 'Invalid Octal number')

        if system1 == 'Hexadecimal':
            for digit in number:
                if not(digit in hexadecimal):
                    return render_template('home.html',result = 'Invalid Hexadecimal number')
    
        if system1 == system2:
            return render_template('home.html',result = number)

        if system1 != 'Hexadecimal':
            try:
                number = int(number)
            except:
                return render_template('home.html',result = 'Invalid Number.')

        number = globals()[f'{system1}To{system2}'](number)
        return render_template('home.html',result = number)
