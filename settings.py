import os

PATH_PROJECT_SRC = os.getcwd()

PATH_LOGS = os.path.join(
    PATH_PROJECT_SRC,
    'logs', 'app.log'
)

STRINGS = os.environ['STRINGS']
#STRINGS = "aba,aba,ab"