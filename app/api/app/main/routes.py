from flask import Flask, jsonify, request, Blueprint, render_template

from app.utilities import GrammarChecker

bp = Blueprint("main", __name__)

from app.main import bp


@bp.route("/")
def index():
    return render_template("main/index.html")


@bp.route("/test-predict", methods=["POST"])
def test_predict():
    text = request.form.get("some_text")

    try:
        pred = predict(text)
    except Exception as e:
        pred = {"error": f"Something went wrong: {e}"}
    return render_template("main/index.html", pred=pred)


@bp.route("/predict", methods=["POST"])
def predict(text=None, data=None):
    gc = GrammarChecker()

    if data:
        data = request.json

    if text:
        predictions = gc.predict_func(text, "i am become death, destroyer of worlds")
    else:
        try:
            sample = data["orig_text", "suggested_text"]
        except KeyError:
            return jsonify({"error": "No text sent"})

        # sample = [sample]
        predictions = gc.predict_func(sample)

    if text:
        return predictions[0]
    try:
        result = jsonify(predictions[0])

    except TypeError as e:
        result = jsonify({"error": str(e)})
    return result

