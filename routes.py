from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username':'HARSHgill'}
    return '''
<html>
  <head>
    <title>Home Page-micro_blog</title>
</head>
<body bgcolor='blue'>

  <h1>Hello,'''+user['username']+'''!<h1>
 </body>
</html> '''
