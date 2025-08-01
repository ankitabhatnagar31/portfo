#server1.py
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def page_name(page_name):
	return render_template(page_name)

@app.route('/index.html')
def my_index():
	return render_template('index.html')

@app.route('/works.html')
def my_works():
	return render_template('works.html')

@app.route('/about.html')
def my_about():
	return render_template('about.html')

@app.route('/contact.html')
def my_contact():
	return render_template('contact.html')

# we will now try to make it dynamic 

#@app.route('/<string:page_name>')
#def page_name(page_name):
	#return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		print("WWWWWWWWWWWRRRRRRRRRRRRIIIIIIIITTTTTTTTTTIIIIIIIIIIIINNNNNNNNNNNNNGGGGGGGGGGGG")
		file = database.write(f'\n {email}, {subject}, {message}')
		print(file)

def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database2:
	    email = data['email']
	    subject = data['subject']
	    message = data['message']
	    csv_writer = csv.writer(database2, delimiter= ',',quotechar='"', quoting=csv.QUOTE_MINIMAL ) 
	    csv_writer.writerow([email, subject, message])  		

@app.route('/submit_form', methods = ['POST','GET'])
def submit_form():
	if request.method=="POST":
		try:
		     data = request.form.to_dict()
		     #print (data)
		     #now we can store this data also in file 'database.txt'
		     #write_to_file(data)
		     write_to_csv(data)
		     #return "Form Submitted"
		     #or we can redirect to a thank you page
		     return redirect('/thankyou.html')
		except:
			  return "Did not save to database"
	else:
		return "Something went wrong! Try again"

#right now we are having server and browser on same computer, that means no one but only us can access the web page that we have created  which we dont want.
#Now to have this webpage accessed by anuone wwill use python anywhere which allows us to host all the files we have to a server for free.
# we just need to create an account on python anywhere.