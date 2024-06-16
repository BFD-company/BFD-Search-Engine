from flask import Flask, request, render_template
import wikipedia

website = Flask(__name__)

@website.route('/', methods=["POST", "GET"])
@website.route('/search', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        wikipedia.set_lang("ar")
        print("Searching...")
        user = request.form.get("user")
        query = wikipedia.search(user)
        links = ""
        for q in query:
            try:
                links += (f"        <div class='link'><a href='https://ar.wikipedia.org/wiki/{q}'>{q}</a><br>{wikipedia.summary(q, 1)}<br></div>")
            except:
                pass
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BFD - Search</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

    <style>
        * {
            font-family: "Exo 2";
            color: white;
            padding: 0;
            margin: 0;
        }

        a {
            color: #0000EE;
            text-decoration: none;
        }

        body {
            background: rgb(48, 48, 48);
        }

        header {
            background: rgb(29, 29, 29);
            width: 100%;
            height: 60px;
        }

        header h1 {
            position: absolute;
            padding: 7px;
        }

        header form {
            position: absolute;
            padding-top: 5px;
            left: 50%;
            transform: translate(-50%);
            width: 50%;
        }

        header input {
            background: rgb(51, 51, 51);
            width: 60%;
            height: 45px;
            padding-right: 10px;
            border-radius: 50px 0 0 50px;
            border: 1px solid gray;
        }

        header button {
            background: rgb(51, 51, 51);
            width: 10%;
            height: 45px;
            border-radius: 0 50px 50px 0;
            border: 1px solid gray;
        }

        footer {
            background: rgb(29, 29, 29);
            width: 100%;
            position: fixed;
            bottom: 0px;
            padding: 5px;
        }

        .link {
            padding: 10px;
            width: 500px;
            height: 150px;
            background: rgb(48, 48, 48);
            border-bottom: 1px solid gray;
        }
    </style>

</head>
<body>
    <header>
        <h1>BFD Search Engine</h1>
        <form method="post">
            <input type="text" name="user">
            <button>Search</button>
        </form>
    </header>
    <div class="links">
        thelinks
    </div>
    <footer><p>CopyRight: ©BFD - Beta For Develop</p></footer>
</body>
</html>""".replace("thelinks", links)

    return render_template("index.html")

website.run(host="0.0.0.0", port=4040)