from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    """
    Function to check the strength of a password.
    """
    # Define password criteria
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Scoring system
    score = sum([length_criteria, upper_criteria, lower_criteria, number_criteria, special_criteria])
    
    # Categorize password strength
    if score < 3:
        strength = "Weak"
        feedback = "Consider making your password longer and adding uppercase letters, numbers, and special characters."
    elif score == 3 or score == 4:
        strength = "Moderate"
        feedback = "Your password is okay but can be improved with more diverse character types or increased length."
    else:
        strength = "Strong"
        feedback = "Your password is strong. Good job!"
    
    return strength, feedback

@app.route('/', methods=['GET', 'POST'])
def password_checker():
    """
    Render the main password checker page.
    """
    if request.method == 'POST':
        password = request.form['password']
        strength, feedback = check_password_strength(password)
        return render_template('result.html', strength=strength, feedback=feedback, password=password)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
