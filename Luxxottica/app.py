from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#import spacy
#from spacy.cli.download import download
#download(model="en_core_web_sm")

app = Flask(__name__)

def train(bot, lang):
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train(("chatterbot.corpus." + lang))
    return bot

my_bot = ChatBot(name="Chatterbot", read_only=True)
my_bot = train(my_bot, 'english')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/setLanguage')
def language(lang):
    try:
        my_bot = train(my_bot, lang)
    except:
        print("That language is not available.")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))

if __name__ == "__main__":
    app.run()


