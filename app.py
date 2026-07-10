from flask import Flask, request, redirect
from database import conn, cursor
from encoder import encode, decode
from cache import cache

app = Flask(__name__)


@app.route("/shorten", methods=["POST"])
def shorten():

    long_url = request.form.get("url")

    if not long_url:
        return {"error": "URL is required"}, 400

    # Store URL in database
    cursor.execute(
        "INSERT INTO urls(long_url) VALUES(?)",
        (long_url,)
    )

    conn.commit()

    url_id = cursor.lastrowid

    # Generate short code
    short_code = encode(url_id)

    # Store in cache if Redis is enabled
    if cache:
        cache.set(short_code, long_url)

    return {
        "short_url": f"http://127.0.0.1:5000/{short_code}"
    }


@app.route("/<code>")
def redirect_url(code):

    # Ignore browser favicon request
    if code == "favicon.ico":
        return "", 204

    # Check cache first
    if cache:
        url = cache.get(code)

        if url:
            return redirect(url)

    # Decode Base62 short code
    try:
        url_id = decode(code)

    except ValueError:
        return "Invalid short URL", 400


    # Fetch original URL from database
    cursor.execute(
        "SELECT long_url FROM urls WHERE id=?",
        (url_id,)
    )

    result = cursor.fetchone()


    if result:

        long_url = result[0]

        # Save in cache if Redis is enabled
        if cache:
            cache.set(code, long_url)

        return redirect(long_url)


    return "URL not found", 404



if __name__ == "__main__":
    app.run(debug=True)