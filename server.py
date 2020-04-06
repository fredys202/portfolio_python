from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


# Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


#Database witc txt file
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email =   data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

#Database with csv file
def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		email =   data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])		


# Form Submit 
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	    if request.method == 'POST':
	    	tri:	
		     data = request.form.to_dict()
		     write_to_csv(data)
		     return redirect('/thankyou.html')
		except:
			return'Did not saved to the database'     
     else:
     	return 'Something went wrong.'	