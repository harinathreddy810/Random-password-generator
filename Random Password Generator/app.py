from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# List of names
names = ['Harinath', 'Saiteja', 'Venu', 'Mahi','Naveen','Harshini','Mounika','Swathi','Vyshu']

def generate_password(length, use_digits, use_special):
    # Pick a random name from the list
    random_name = random.choice(names)

    # Create password with a fixed name length
    password = random_name

    if use_special:
        password += '@'  # Adding the special character
    
    # Generate a random number if digits are requested
    if use_digits:
        random_number = ''.join(random.choices(string.digits, k=length - len(password)))
        password += random_number

    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        use_digits = 'digits' in request.form
        use_special = 'special' in request.form
        password = generate_password(length, use_digits, use_special)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
