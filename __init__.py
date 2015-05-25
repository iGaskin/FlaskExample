from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    title = "Epic Tutorials"
    paragraph = ["wow I am learnign so much great stuff!","stuff 2", "stuff3"]

    return render_template("index.html", title = title, paragraph=paragraph)


@app.route('/about')
def about():
    title = "About this site"
    paragraph = ["This is a test framework that I am develping using Flask"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)


if __name__ == "__main__":
    app.run()
