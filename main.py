import sys
import logging
from flask import Flask
from flask_restplus import Api, Resource, fields
from settings import STRINGS
from SparseArray import SparseArray


flask_app = Flask(__name__)
app = Api(app = flask_app,
          version = "1.1.1",
          title = "SparceArrayCreator",
          description = "Gives you sparse representation of a given string for input query")

name_space = app.namespace('MDM', description='create sparseArray')

model = app.model('Sentence',
                  {'strings': fields.String(required = True,
                                         description="string to represent as a SparseArray",
                                         help="strings cannot be blank.")})

@name_space.route("/create/<string:query>")
class MainClass(Resource):
    @app.doc(responses={200: 'OK', 400: 'Invalid Argument'},
             params={'query': 'Specify the query to look after in our defined string'})
    def get(self, query):
        try:
            #sparsed_string = sparse_array.sparse_it(query=query)
            return {
                "status": "String formated in SparseArray",
                "SparseArray": "LOL"
            }
        except Exception as e:
            name_space.abort(400, e.__doc__, status="the given query is empty", statusCode="400")


if __name__ == '__main__':
    flask_app.run(debug=True, host="127.0.0.1", port=5000)

    #get the query with which we'll look for occurences in string
    query = str(sys.argv[1])

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #TODO if length = 0 the raise an exception

    sparse_array = SparseArray(STRINGS)
