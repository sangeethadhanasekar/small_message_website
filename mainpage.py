from flask import Flask,render_template,request
import sqlite3 as sql
from save import save_rec,retrive,create_database
create_database()
app=Flask(  __name__,
        template_folder = "client/template",
)



#@app.route("/submited", methods=['POST', 'GET'])
#def addrec():
   # if request.method == 'POST':
    #        name= request.form['usrname']
   #         post =request.form['posttxt']
  #          msg=save_rec(name, post)
 #           return render_template("result.html", msg=msg)

@app.route('/',methods=['POST', 'GET'])
def list():

   if request.method=='GET':
       rows = retrive()
       return render_template('page1.html', rows=rows)
   else:
      name = request.form['usrname']
      post = request.form['posttxt']
      msg = save_rec(name, post)
      rows=retrive()
      return render_template("page1.html",rows=rows)


if __name__ == "__main__":
    app.run(debug=True)