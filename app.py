"""
Changelog
0.1 - Created App, Bug Fixes
0.2 - Added new page
0.2.1 - Bug Fixes
0.2.2 - Added description, which color to use (HEX)
0.3 - Added TinyURL Integration, Code Optimization
0.3.1 - Bug Fixes
0.3.2 - And Again...
"""

from flask import Flask, request
from pyshorteners import Shortener, Shorteners
from pyshorteners.exceptions import ShorteningErrorException
import random
app = Flask(__name__)
s = Shortener(Shorteners.TINYURL)
a = '<meta name="viewport" content="width=device-width,initial-scale=1">By DanilMirov#7485 (ID: 321268938728144906)<br>'
@app.route('/')
@app.route('/make/embed')
def embedmaker():
    return a+'''
Embed for Discord
<form action="/embed">
    Text:<br><input type="text" name="text"><br>
    Title:<br><input type="text" name="title"><br>
    Image:<br><input type="text" name="img"><br>
    Color (HEX):<br><input type="text" name="color"><br>
    <input type="submit">
</form><br><br><a href="{}create/fake/work">Фейк комманада work (от UnbelievaBoat)</a>
'''.format(request.url)
@app.route('/favicon.ico')
def favicon(): return "None"
@app.route('/embed')
def embed():
    ua = request.headers.get('User-Agent')
    fin = ''
    text = request.args.get('text')
    title = request.args.get('title')
    image = request.args.get('img')
    color = request.args.get('color')
    if ua == "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)":
        if text: fin += '<meta property="og:description" content="{0}" />'.format(text)
        if title: fin += '<meta property="og:title" content="{0}" />'.format(title)
        if image: fin += '<meta property="og:image" content="{0}" />'.format(image)
        if color: fin += '<meta name="theme-color" content="{0}">'.format(color)
        if not color: fin += '<meta name="theme-color" content="#233d8c">'
    else: fin += a
    fin += 'Теперь скопируйте и вставьте эту ссылку в дискорд!'
    fin += '<br>Короткая ссылка - {}'.format(s.short(request.url))
    return fin
@app.route('/work')
def work():
    ua = request.headers.get('User-Agent')
    fin = ''
    name = request.args.get('name')
    currency = request.args.get('currency')
    money = str(random.randint(9999999, 999999999))
    if ua == "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)":
        if name: fin += '<meta property="og:title" content="{0}" />'.format(name)
        if not name: fin += '<meta property="og:title" content="NoName" />'
        if currency: fin += '<meta property="og:description" content="Ты работал в Ебеньграде и получил {0}{1}" />'.format(currency, money)
        if not currency: fin += '<meta property="og:description" content="Ты работал в Ебеньграде и получил ${0}" />'.format(money)
        fin += '<meta name="theme-color" content="#66BB6A">'
    else: fin += a
    fin += 'Теперь скопируйте и вставьте эту ссылку в дискорд!'
    fin += '<br>Короткая ссылка - {}'.format(s.short(request.url))
    return fin
@app.route('/create/fake/work')
def fakework():
    return a+'''
Embed for Discord
<form action="/work">
    Currency<br><input type="text" name="currency"><br>
    Name:<br><input type="text" name="name"><br>
    <input type="submit">
</form>
'''

if __name__ == '__main__': app.run(debug=True)
