from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '''<p>This was the beginning, how to become uncontaminated. We have got some attachment to the material modes of nature. That is the cause of our bondage. Now, if we want to be free from this bondage, uncontaminated, then the same attachment should be transferred to the sadhu. Sa eva sadhusu krtah, the same attachment. Everyone has got attachment. Nobody is free of attachment. The Mayavadi philosophy, they say that "Stop this attachment." The Buddha philosophy says that "Make this attachment zero." This is also a little advancement, but it is not possible to make our attachment zero. That is not possible. Therefore Bhagavan says in the Bhagavad..., param drstva nivartate [Bg. 9.59]. Just like a child has got attachment for playing, and gradually, his attachment should be transferred for reading, going to school, education. But if you stop his attachment, then he will become mad. You must give something. Param drstva nivartate. Just like we are. To the Western devotees, we are advising them -- at least, those who are accepted as our disciples, they must -- no meat-eating. They are accustomed to meat-eating, but that how this meat-eating has been stopped? We have given them nice things, kacuris, srngara, rasagulla. So they have given up meat-eating. So you must give something more palatable. Then detachment will be possible. First of all nullify the attachment, and then give him better attachment. Then he will forget. Param drstva nivartate. You cannot force a living entity by force. Gradually... The same example: a child has got attachment, but by some system, its attachment is turned over.</p>'''


if __name__ == "__main__":
    app.run(debug=True)
