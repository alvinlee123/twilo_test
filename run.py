from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
    "+15107120735": "Alvin Lee",
    }

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    from_number = request.values.get('From',None)
    resp = twilio.twiml.Response()

    if from_number in callers:
        #Greet caller by name
        resp.say("Hello " + callers[from_number])
    else:
        resp.say("FUCK YOU")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)












