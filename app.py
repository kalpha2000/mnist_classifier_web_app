from flask import Flask,render_template,request
from util import pred_digit
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html',prediction=None)
    else:
        img_path = r'./project/web app ml/digit classifier/digit.jpg'
        request.files.get('digit').save(img_path)
        pred = pred_digit(img_path)
        return render_template('home.html',prediction=pred)






# only run this app.py when its the file that is executed
if __name__ == '__main__':
    # bascilly we wont have to restart whenever a change is made
    app.run(use_reloader=True, debug=True)