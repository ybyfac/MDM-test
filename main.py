""" entrypoint of this app"""
import json
from flask import Flask
from flask_restplus import Api, Resource, fields
from settings import STRINGS
from SparseArray import SparseArray


FLASK_APP = Flask(__name__)
APP = Api(app=FLASK_APP,
          version="1.1.1",
          title="SparceArrayCreator",
          description="Gives you sparse representation of a given string for input query")

NAME_SPACE = APP.namespace('SparseArray', description='create sparseArray')

MODEL = APP.model('Sentence',
                  {'strings': fields.String(required=True,
                                            description="string to represent as a SparseArray",
                                            help="strings cannot be blank.",
                                            default='aba,ab'
                                            )
                   })

@NAME_SPACE.route("/create/<string:query>")
class MainClass(Resource):
    """ class is made to handle Flask Swagger API exposition
    """
    @APP.doc(responses={200: 'OK', 400: 'Invalid Argument'},
             params={'query': 'Specify the query to look after in our defined string'},
             default='aba,ab')
    def get(self, query):
        """
           Method expose the api sparse_it method of sparse_array class and module
            Args:
                - query (str): scenario name specified in settings file
        """
        try:
            sparsed_string = SPARSE_ARRAY.sparse_it(query=query)
            sparsed_string_json = json.dumps(sparsed_string)

            return {
                "status": "String formated in SparseArray",
                "SparseArray": sparsed_string_json
            }
        except Exception as exception:
            NAME_SPACE.abort(400, exception.__doc__,
                             status="the given query is empty",
                             statusCode="400")


if __name__ == '__main__':
    # get the query with which we'll look for occurences in string
    # query = str(sys.argv[1])

    SPARSE_ARRAY = SparseArray(STRINGS)

    FLASK_APP.run(debug=False, host="0.0.0.0")
    # flask_app.run(debug=False, host="127.0.0.1", port=5000)