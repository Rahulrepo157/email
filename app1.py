# -*- coding: utf-8 -*-
"""Untitled124.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GEWGjsKl-C6VrlGoCEsiaA0-bq5WLxpO
"""







from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the feedback form
@app.route('/')
def feedback_form():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Feedback Form</title>
    </head>
    <body>
        <h2>Feedback Form</h2>
        <form action="/submit" method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br><br>
            <label for="feedback">Feedback:</label><br>
            <textarea id="feedback" name="feedback" rows="4" cols="50" required></textarea><br><br>
            <label for="rating">Rating (1-5):</label><br>
            <input type="number" id="rating" name="rating" min="1" max="5" required><br><br>
            <div id="reasonDiv" style="display:none;">
                <label for="reason">Reason for low rating:</label><br>
                <textarea id="reason" name="reason" rows="2" cols="50"></textarea><br><br>
            </div>
            <button type="submit">Submit</button>
        </form>
        <script>
            const ratingInput = document.getElementById('rating');
            const reasonDiv = document.getElementById('reasonDiv');
            ratingInput.addEventListener('input', function() {
                if (ratingInput.value < 3) {
                    reasonDiv.style.display = 'block';
                } else {
                    reasonDiv.style.display = 'none';
                }
            });
        </script>
    </body>
    </html>
    '''

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']
    rating = int(request.form['rating'])
    reason = request.form.get('reason', '')  # Optional field

    # Save feedback to a file (or database)
    with open('feedback.csv', 'a') as file:
        file.write(f"{name},{email},{feedback},{rating},{reason}\n")

    return f'''
    <h2>Thank you for your feedback, {name}!</h2>
    <p>We appreciate your time in helping us improve.</p>
    <a href="/">Submit Another Feedback</a>
    '''

if __name__ == '__main__':
    app.run(debug=False)


