app = Flask(__name__)
model = joblib.load('model')

@app.route('/',methods=['GET'])
def index ():
    return render_template('inputform.html')

@app.route('/',methods=['POST'])
def input ():
    csv_file = request.files.get('myfile')
    file = pd.read_csv(csv_file,sep= ',',index_col=0,encoding='utf-8')
    file['prediction'] = model.predict(file)
    return file.to_html()

if __name__ == '__main__':
    app.run(host='127.0.0.7',port='5000')
