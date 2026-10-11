from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "Number Info API is running",
        "usage": "/info?number=PHONE_NUMBER",
        "note": "This demo validates phone-number format only and does not retrieve private subscriber information."
    })

@app.get("/info")
def number_info():
    number = request.args.get("number", "").strip()

    if not number:
        return jsonify({"error": "Please provide the ?number= parameter."}), 400

    # Accept digits with an optional leading +. Spaces and punctuation are rejected.
    if not re.fullmatch(r"\+?\d{7,15}", number):
        return jsonify({
            "error": "Invalid phone number format.",
            "hint": "Use 7–15 digits, optionally prefixed with +."
        }), 400

    return jsonify({
        "number": number,
        "valid_format": True,
        "message": "Format accepted. This API does not look up or disclose a person's name, address, location, device identifiers, or tracking history."
    })

@app.errorhandler(404)
def not_found(_error):
    return jsonify({"error": "Endpoint not found."}), 404

@app.errorhandler(405)
def method_not_allowed(_error):
    return jsonify({"error": "Method not allowed."}), 405

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
