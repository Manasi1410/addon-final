from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    color = "#FFFFFF"
    if request.method == 'POST':
        try:
            height_cm = float(request.form['height'])
            weight_kg = float(request.form['weight'])
            height_m = height_cm / 100
            bmi = round(weight_kg / (height_m ** 2), 2)
            
            if bmi < 18.5:
                category = "Underweight"
                color = "#89CFEF"   # Baby Blue
            elif bmi < 25:
                category = "Normal"
                color = "#73C2FB"   # gold
            elif bmi < 30:
                category = "Overweight"
                color = "#57A0D2"   # darker gold
            else:
                category = "Obese"
                color = "#0E4C92"   #Navy Blue
        except (ValueError, ZeroDivisionError):
            bmi = None
            category = "Invalid input"
            color = "red"

    return render_template('index1.html', bmi=bmi, category=category, color=color)

if __name__ == "__main__":
    app.run(debug=True)