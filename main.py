from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
import nltk

nltk.download('vader_lexicon')

app = Flask(__name__)

print(type(request))
@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        if isinstance(request, str):
            # If request is a string, it might be an unexpected value
            return render_template('home.html', message="Invalid request")
        
        inp = request.form.get("inp")
        sid = sia()
        score = sid.polarity_scores(inp)
        compound_score = score["compound"]

        if compound_score >= 0.5:
            return render_template('home.html', message="Very Positive", confidence=compound_score)
        elif 0.2 <= compound_score < 0.5:
            return render_template('home.html', message="Positive", confidence=compound_score)
        elif -0.2 < compound_score < 0.2:
            return render_template('home.html', message="Neutral", confidence=compound_score)
        elif -0.5 <= compound_score < -0.2:
            return render_template('home.html', message="Negative", confidence=compound_score)
        else:
            return render_template('home.html', message="Very Negative", confidence=compound_score)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)

#Somehow it works. Fuck.

#well, plan selanjutnya
#Coba integrasi algoritm yang lebih sophispicated ti Flask
#Buat rating prediction system.