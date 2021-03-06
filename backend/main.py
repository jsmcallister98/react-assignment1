from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello():
    return 'Hello'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_jobname = request.args.get('job')
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         if search_jobname :
            subdict2 = {'users_list' : []}
            for user in subdict['users_list']:
               if user['job'] == search_jobname:
                  subdict2['users_list'].append(user)
            return subdict2
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp      

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id :
      if request.method == 'GET':
         for user in users['users_list']:
            if user['id'] == id:
               return user
            return ({})
         return users
      elif request.method == 'DELETE':
         for user in users['users_list']:
            if user['id'] == id:
               users['users_list'].remove(user)
               return user
         return jsonify(success=False)         

      