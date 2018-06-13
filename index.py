from flask import Flask, request, render_template, jsonify
import os.path
import sqlite3
from database import Client, ProductArea, FeatureRequest, DBSession
from invalid_usage import InvalidUsage

app = Flask(__name__)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html', name=name)

@app.route('/client')
def client():
    list = DBSession().query(Client).all()
    return jsonify([e.to_json() for e in list])

@app.route('/product_area')
def product_area():
    list = DBSession().query(ProductArea).all()
    return jsonify([e.to_json() for e in list])

@app.route('/feature_request', methods=['GET', 'POST'])
@app.route('/feature_request/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def feature_request(id = None):
    if request.method == 'GET':
        if id == None:
            list = DBSession().query(FeatureRequest).all()
            return jsonify([e.to_json() for e in list])
        else:
            try:
                fr = DBSession().query(FeatureRequest).filter(FeatureRequest.id == id).one()
                return jsonify(fr)
            except:
                raise InvalidUsage('404 Not found', status_code=404, payload='404 Not found')
    elif request.method == 'POST':
        if id == None:
            frJson = request.get_json(force=False)
            title = frJson['title']
            description = frJson['description']
            client_id = frJson['client_id']
            client_priority = frJson['client_priority']
            target_date = frJson['target_date']
            product_area_id = frJson['product_area_id']
            fr = FeatureRequest()
            fr.title = title
            fr.description = description
            fr.client_id = client_id
            fr.client_priority = client_priority
            fr.target_date = target_date
            fr.product_area_id = product_area_id
            DBSession().add(fr)
            DBSession().flush()
            DBSession().commit()
            return jsonify(fr)
        else:
            raise InvalidUsage('Method not allowed', status_code=405, payload='Method not allowed')
    elif request.method == 'PUT':
        if id != None:
            try:
                fr = DBSession().query(FeatureRequest).filter(FeatureRequest.id == id).one()
                frJson = request.get_json(force=False)
                title = frJson['title']
                description = frJson['description']
                client_id = frJson['client_id']
                client_priority = frJson['client_priority']
                target_date = frJson['target_date']
                product_area_id = frJson['product_area_id']
                fr.title = title
                fr.description = description
                fr.client_id = client_id
                fr.client_priority = client_priority
                fr.target_date = target_date
                fr.product_area_id = product_area_id
                DBSession().flush()
                DBSession().commit()
                return jsonify(fr)
            except:
                raise InvalidUsage('404 Not found', status_code=404, payload='404 Not found')
        else:
            raise InvalidUsage('Method not allowed', status_code=405, payload='Method not allowed')
    elif request.method == 'DELETE':
        if id != None:
            try:
                fr = DBSession().query(FeatureRequest).filter(FeatureRequest.id == id).one()
                DBSession().delete(fr)
                return jsonify(True)
            except:
                raise InvalidUsage('404 Not found', status_code=404, payload='404 Not found')
        else:
            raise InvalidUsage('Method not allowed', status_code=405, payload='Method not allowed')
    else:
        raise InvalidUsage('Method not allowed', status_code=405, payload='Method not allowed')


if __name__ == "__main__":
    app.run()
