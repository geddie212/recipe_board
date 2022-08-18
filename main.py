from flask import Flask, render_template, request
import nutrition_api

app = Flask(__name__)


@app.route('/recipe/<int:id>')
def recipe(id):
    recipe_info = nutrition_api.RecipeAPI(id).return_data()
    return render_template('recipe.html', recipe=recipe_info)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    filters = {}
    if request.method == 'POST':
        for field in request.form:
            filters[field] = request.form[field]
    api = nutrition_api.NutritionAPI(filters)
    api.query_stringer()
    recipe_results = api.send_request()
    result_list = []
    final_list = []
    column = 0

    for rec in recipe_results['results']:
        result_list.append(rec)
        column += 1
        if column == 5:
            final_list.append(result_list)
            result_list = []
            column = 0
    return render_template('results.html', results=final_list, query=filters['query'])


if __name__ == '__main__':
    app.run(debug=True)
