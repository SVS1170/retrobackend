import os

from aiohttp import web
import aiohttp_jinja2
import jinja2
# import postgres_connect as pgc

login = 'COCK'
password = 'SUCK'
name = 'TEST'
firstname = 'TEST1'
email = 'GAVNO@GMAIL.COM'


async def handle(request: web.Request) -> web.StreamResponse:
    # text = f'''<form method="post" action="/">
    #     <table>
    #         <tr>
    #             <td><label for="loginField">Кто ты?</label></td>
    #             <td><input id="loginField" type="text" name="login"></td>
    #         </tr>
    #         <tr>
    #             <td><label for="passwordField">Пароль</label></td>
    #             <td><input id="passwordField" type="password" name="password"></td>
    #         </tr>
    #         <tr>
    #             <td colspan="2" style="text-align: center"><input type="submit" value="Наступи в меня"></td>
    #         </tr>
    #     </table>
    # </form>'''
    context = {
        'current_date': 'January 27, 2017'
    }
    response = aiohttp_jinja2.render_template("login.html", request,
                                          context=context)
    return response

async def wmnk1(request) -> web.StreamResponse:
    global login
    global password
    a = await request.post()
    # print(a)
    x1 = (a["login"])
    x2 = (a["password"])

    # text = pgc.read_data(x1)
    print(f"login : {x1}\npassword : {x2}")
    # print(result)

    if (x1 == login):
        if (x2 == password):
            # text = pgc.read_data(x1)[0] + " " + pgc.read_data(x1)[1]
            text = f'''<!DOCTYPE html>
                    <html>
                    <h1><h1/>
                    <h1><h1/>
                    <form action="/mnk">
                       <a href="https://www.youtube.com/watch?v=eHqqENg69EA">Go to YouTube</a>
                    </form>
                    </html>'''
        else:
            # text = pgc.read_data(x1)[0] + " " + pgc.read_data(x1)[1]
            text = f'''<!DOCTYPE html>
                        <html>
                        <h1><h1/>
                        <form action="/mnk">
                           <a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjk3OLhlt_2AhXjlIsKHbUnA9EQFnoECAcQAQ&url=http%3A%2F%2Fgayporka.top%2F&usg=AOvVaw1z03s7x5DN1tMRrMdkLhNd">Go to Nahui</a>
                        </form>
                        </html>'''

    else :
        # text = pgc.read_data(x1)[0] + " " + pgc.read_data(x1)[1]
        text = f'''<!DOCTYPE html>
            <html>
            <h1><h1/>
            <form action="/mnk">
               <button class="test"></button>
            </form>
            </html>'''

    # return web.Response(text=text, content_type='text')
    return web.Response(text=text, content_type='text/html')

app = web.Application()
aiohttp_jinja2.setup(
    app, loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), "templates")))
app.add_routes(
    [
     web.static('/', "../retrobackend/static"),
     web.get("/login", handle),
     # web.get("/mnk", wmnk),
     web.post("/", wmnk1),
     # web.post("/registration", wmnk2),
     # web.get("/registration", wmnk2),
     # web.get("/login", wmnk3),
     web.post("/login", wmnk1),
     # web.get("/feedback", wmnk4),
     # web.post("/feedback", wmnk4),
     web.get("/{name}", handle)])

web.run_app(app)