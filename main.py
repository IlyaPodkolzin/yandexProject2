from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    engineer_prof = False
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        engineer_prof = True
    return render_template('training.html', engineer_prof=engineer_prof)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    prof_list = ["Инженер-исследователь", "Пилот", "Строитель", "Экзобиолог",
                 "Врач", "Инженер по терраформированию", "Климатолог", "Специалист по радиационной защите",
                 "Астрогеолог", "Гляциолог", "Инженер жизнеобеспечения", "Метеоролог",
                 "Оператор марсохода", "Киберинженер", "Штурман", "Пилот дронов"]
    return render_template('list_prof.html', prof_list=prof_list, list_type=list_type)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
