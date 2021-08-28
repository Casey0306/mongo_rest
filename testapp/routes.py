from flask import jsonify, request
from testapp import app
from testapp import mondb
from testapp import util


@app.route('/create', methods=['POST'])
def create_item():
    data = request.get_json()
    dict_json = {}
    dict_json["name"] = data["name"]
    dict_json["description"] = data["description"]
    dict_json["parameters"] = data["parameters"]
    mondb.create_item(collection_name=data["collection"], params=dict_json)
    return jsonify({"response": "Item successfully created"}), 201


@app.route('/find', methods=['POST'])
def find_item_params():
    data = request.get_json()
    dict_json = util.dict_parser(data)
    result = mondb.find_item(collection_name=data["collection"],
                             params=dict_json)
    return jsonify({"result": result}), 200


@app.route('/find', methods=['GET'])
def find_item_detail():
    item_id = request.args.get('id', default='*', type=str)
    collection = request.args.get('colname', default='*', type=str)
    result = mondb.find_item_detail(collection_name=collection,
                                    param_id=item_id)
    return jsonify({"result": result}), 200
