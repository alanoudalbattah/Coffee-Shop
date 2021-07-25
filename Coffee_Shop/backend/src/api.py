import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from sqlalchemy.sql.elements import Null

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
db_drop_and_create_all()

# ROUTES
'''
✅@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['GET'])
def drinks(): return jsonify({ 'success': True, 'drinks': [drinks.short() for drinks in Drink.query.all()]}), 200


'''
✅@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def drinks_details(payload):# <-- must take 1 postional args
    return jsonify({ 'success': True, 'drinks': [drinks.long() for drinks in Drink.query.all()] }), 200

'''
✅@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drinks(payload):   
    title = request.get_json()['title'], recipe = request.get_json()['recipe'] # fetch values from request body 

    if type(recipe) != type([]): # in case recipe is not an array
        abort(400,  description='recipe must be an array')
        # using custom abort message src: https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
        
    new_drink = Drink( title=title , recipe=json.dumps(recipe)) #? (json.dumps) serialize object to JSON formatted string
    
    try:
        new_drink.insert()
    except:
        # since we already checked recipe the only possible error left is title not unique
        abort(400, {'description': 'title must be unique'})
    
    return jsonify({ 'success': True, 'drinks': [new_drink.long()] }), 200

'''
✅@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drinks(payload, _id):
    title = request.get_json()['title'], recipe = request.get_json()['recipe'] # fetch values from request body 

    updated_drink = Drink.query.get_or_404(_id)
    
    if type(recipe) != type([]): # in case recipe is not an array
         abort(400,  description='recipe must be an array')

    updated_drink.title = title 
    updated_drink.recipe = json.dumps(recipe)
    
    try:
        updated_drink.update()
    except:
        abort(400, description='title must be unique') # in case title is not unique

    return jsonify({ 'success': True, 'drinks': [updated_drink.long()]}), 200

'''
✅@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(payload, _id):
    #? i added a return statement to "delete method" in models.py to make sure the right resource is deleted :)
    return jsonify({ 'success': True, 'delete': (Drink.query.get_or_404(_id).delete()).get('id') }), 200


# Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
'''
✅@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def unprocessable(err):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(400)
def unprocessable(err):
    return jsonify({
        "success": False,
        "error": 400,
        "message": err.description
    }), 400

'''
✅@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def unprocessable(err):
    return jsonify({
        "success": False,
        "error": err.status_code,
        "message": err.error.get('description'),
    }), err.status_code

#src: https://auth0.com/docs/quickstart/backend/python/01-authorization