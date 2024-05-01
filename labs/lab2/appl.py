HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Приветствие</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .cat {
            font-family: monospace;
            font-size: 14px;
            white-space: pre;
        }
    </style>
</head>
<body>
    <h3>Привет!</h3>
    <p>Вот тебе ASCII-кот!:</p>
    <div class="cat">
     /\_/\\ \n
    ( o.o )\n
     > ^ <\n
    </div>
</body>
</html>

"""

def app(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html; charset=utf-8'),
    ]
    start_response(status, response_headers)
    html_as_bytes = HTML.encode('utf-8')
    return [html_as_bytes]
