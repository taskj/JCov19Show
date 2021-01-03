from flask import Flask
from flask import render_template
from flask import jsonify
import string
import utils
from jieba.analyse import extract_tags

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/time')
def gettime():
    return utils.get_time()

@app.route('/l1')
def get_l1_data():
    d = []
    confirm = []
    for item in utils.get_l1_data():
        d.append(item[1].strftime("%Y-%m-%d"))
        confirm.append(int(item[0]))
    return jsonify({"date":d,"confirm":confirm})

@app.route('/l2')
def get_l2_data():
    heal = []
    dead = []
    d = []
    for item in utils.get_l2_data():
        heal.append(int(item[1]))
        dead.append(int(item[0]))
        d.append(item[2].strftime("%Y-%m-%d"))
    return jsonify({"heal":heal,"dead":dead,"date":d})


@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":str(data[0]),"suspect":"暂无","heal":str(data[1]),"dead":str(data[2])})

@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

@app.route('/r1')
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city":city,"confirm":confirm})

@app.route('/r2')
def get_r2_data():
    data = utils.get_r2_data()
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)
        v = i[0][len(k):]
        ks = extract_tags(k)
        for j in ks:
            if not j.isdigit():
                d.append([j,v])
    return jsonify({"kws":d})


if __name__ == '__main__':
    app.run(debug=True)
