import os

from flask import Flask, request
from sklearn import tree
import json

app = Flask(__name__)




@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    return '''<h1>The language value is {}</h1>'''.format(language)


@app.route('/diagnose-porumbescu', methods=['POST', 'GET'])
def diagnose_porumbescu():
    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    arg3 = request.args.get('arg3')
    arg4 = request.args.get('arg4')
    arg5 = request.args.get('arg5')

    if request.method == 'GET':
        X = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0],
             [0, 0, 1, 0, 0], [0, 0, 1, 1, 1],
             [0, 0, 1, 0, 1], [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0], [1, 2, 0, 0, 0], [2, 0, 0, 0, 0],
             [2, 1, 0, 0, 0], [2, 2, 0, 0, 0], [2, 2, 1, 1, 1],
             [3, 0, 0, 0, 0], [3, 1, 0, 0, 0], [3, 2, 0, 0, 0],
             [3, 0, 1, 0, 0], [3, 1, 1, 1, 0], [3, 2, 1, 0, 0],
             [3, 0, 1, 0, 1], [3, 1, 1, 1, 1], [3, 2, 1, 0, 1]]
        Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, Y)
        Z = clf.predict([[arg1, arg2, arg3, arg4, arg5]])
        return '{}'.format(Z)
    else:
        return 'fac of visica'


@app.route('/diagnose-mijlai', methods=['POST', 'GET'])
def diagnose_mijlai():
    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    arg3 = request.args.get('arg3')
    arg4 = request.args.get('arg4')

    if request.method == 'GET':
        X = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
             [0, 0, 0, 1], [1, 0, 0, 0], [1, 0, 0, 1],
             [0, 0, 1, 1], [0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0],
             [0, 1, 1, 0], [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1],
             [0, 1, 1, 1], [1, 1, 1, 1]]
        Y = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, Y)
        Z = clf.predict([[arg1, arg2, arg3, arg4]])
        return '{}'.format(Z)
    else:
        return 'Unable to predict'


# array[1])

# return 'pula'

@app.route('/tree-example')
def tree_example():
    # Make a prediction with a decision tree
    def predict(node, row):
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return predict(node['left'], row)
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return predict(node['right'], row)
            else:
                return node['right']

    dataset = [[2.771244718, 1.784783929, 0],
               [1.728571309, 1.169761413, 0],
               [3.678319846, 2.81281357, 0],
               [3.961043357, 2.61995032, 0],
               [2.999208922, 2.209014212, 0],
               [7.497545867, 3.162953546, 1],
               [9.00220326, 3.339047188, 1],
               [7.444542326, 0.476683375, 1],
               [10.12493903, 3.234550982, 1],
               [6.642287351, 3.319983761, 1]]

    #  predict with a stump
    stump = {'index': 0, 'right': 1, 'value': 6.642287351, 'left': 0}
    for row in dataset:
        prediction = predict(stump, row)
    print('Expected=%d, Got=%d' % (row[-1], prediction))
    return '''<h1>The prediciton value is {} and the expected was{}</h1>'''.format(prediction, row[-1])


@app.route('/form-example', methods=['GET', 'POST'])  # allow  both GET and POST requests
def form_example():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1>The language value is: {}</h1>
				  <h1>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
				  Language: <input type="text" name="language"><br>
				  Framework: <input type="text" name="framework"><br>
				  <input type="submit" value="Submit"><br>
			  </form>'''


@app.route('/json-example', methods=['POST'])  # GET r  quests will be blocked
def json_example():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python']  # two k  ys are needed because of the nested object
    example = req_data['examples'][0]  # an in  ex is needed because of the array
    boolean_test = req_data['boolean_test']

    return

    '''
		   The language value is: {}
		   The framework value is: {}
		   The Python version is: {}
		   The item at index 0 in the example list is: {}
		   The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


@app.route('/test-me')
def objectTest():
    a = {'result': 5}
    payload = json.dumps(a)
    return payload


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
