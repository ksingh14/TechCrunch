from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    return """<html>
                   <head>
                      <script type="text/javascript" src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
                      <script>
                           $(document).ready(function(){

                                $('#btnSend').click(function(){

                                    $.ajax({
                                      type: 'POST',
                                      url: '/process',
                                      success: function(data){
                                        alert(data);
                                      }
                                    });
                                });

                           });
                      </script>
                   </head>
                   <body>
                   Skillset: <input type="text" name="skillset"><br>
                    <input type="button" id="btnSend" value="process">
                    </body>
                   </html>"""


@app.route('/process', methods=['POST'])
def view_do_something():

    if request.method == 'POST':
        #your database process here
        return "OK"
    else:
        return "NO OK"

if __name__ == '__main__':
    app.run()