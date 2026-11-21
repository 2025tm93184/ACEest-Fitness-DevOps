from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/members")
def members():
    members_list = [
        {
            "id": 1,
            "name": "Rahul",
            "membership": "Premium",
            "status": "Active"
        },
        {
            "id": 2,
            "name": "Priya",
            "membership": "Standard",
            "status": "Active"
        },
        {
            "id": 3,
            "name": "Arjun",
            "membership": "Premium",
            "status": "Active"
        }
    ]

    return render_template(
        "members.html",
        members=members_list
    )


@app.route("/api/members")
def api_members():
    members_list = [
        {
            "id": 1,
            "name": "Rahul",
            "membership": "Premium",
            "status": "Active"
        },
        {
            "id": 2,
            "name": "Priya",
            "membership": "Standard",
            "status": "Active"
        },
        {
            "id": 3,
            "name": "Arjun",
            "membership": "Premium",
            "status": "Active"
        }
    ]

    return jsonify(members_list)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "ACEest Fitness & Gym",
        "version": "1.0"
    }), 200
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )