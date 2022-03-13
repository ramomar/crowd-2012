from bottle import template, route, request, run
from pymongo import Connection
import operator
#DBURI = "user:password@staff.mongohq.com:10012/DB_NAME"
DBNAME = ""
collection = "grupo209"

#connection = Connection(host=DBURI)
connection = Connection()
db = connection[DBNAME]

@route('/newdocument/:documentname')
def newDocument(documentname):
    db[collection].insert({"document_name":documentname})
    
@route('/')
def index():
    return template('templates/index')

@route('/wait')
def wait():
    return template('templates/wait')

@route('/showquestions')
def showQuestions():
    questions = []
    obj = db[collection].find()
    l = True
    i = 0
    while(l == True):
        try:
            d = obj[i]
            d.pop("_id")
            questions.append(d)
            i = i+1
        except(IndexError):
            l = False
            questions.sort(key=operator.itemgetter('question_number')) # sort list by 'question_number'
            return template('templates/showquestions', aQuestions=questions)

@route('/newquestion')
def newQuestion():
    return template('templates/newquestion')

@route('/newquestion', method='POST')
def writeQuestion():
    question = request.forms.question
    questionNumber = int(request.forms.number)
    answer = request.forms.answer

    if(questionNumber == 0):
        return "<p>El numero de la pregunta no debe ser cero.</p>"
    elif(len(question) == 0 or len(answer) == 0):
        return "<p>Datos no validos, porfavor no uses caracteres especiales(acentos, signos de interrogacion, etc.).</p>"

    else:
        entity = {"question_number": questionNumber,
             "question": question,
             "answer": answer
             }
             
        if(db[collection].find_one({"question_number": questionNumber}) != None):
            return "<p>Esa pregunta ya se contesto. Revisa el numero o haz otra.</p>"
        else:
            db[collection].insert(entity)
            print("Entity saved to the DB.")
            return "<p>Muchas gracias (:</p>"
    
run(host = '0.0.0.0', port = 80, server='cherrypy')
