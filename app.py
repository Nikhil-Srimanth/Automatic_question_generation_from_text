from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from flask import Flask,render_template,redirect,url_for,request



app = Flask(__name__)

try:
    model_path = "./final_model_test"

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    qg_pipeline = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer
    )
except Exception as e:
    print("Model not found")

@app.route('/')
def main():
    
    return render_template("index.html")
@app.route('/gen',methods=["POST","GET"])
def gen():
    passage = request.form['Paragraph']
    result = qg_pipeline(
        "generate question: " + passage,
        max_new_tokens=64,
        do_sample=False
    )
    
    return render_template("index.html",Quess=result)
if __name__ == "__main__":
    app.run(debug=True)