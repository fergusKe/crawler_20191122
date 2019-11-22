# 把以下程式放到 .py 上執行
# 執行後，伺服器會持續開著
# 到瀏覽器開啟 http://127.0.0.1:5000/ 就可以看到網頁
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
      <head>
        <title>網頁標題</title>
      </head>
      <body>
        <div id="header">
          <a class="logo" href="https://test.com.tw/logo-link">
            PTT
          </a>
        </div>
        <div class="images">
          <img src="0.png" />
          <img src="01.png" />
          <img src="02.png" />
          <img src="03.png" />
          <img src="11.png" />
          <img src="12.png" />
          <img src="13.png" />
          <img src="01111.png" />
        </div>
        <div id="container">
          <h2 id="title">八卦版</h2>
          <div class="article a1">
            <h3 class="title t1">文章標題1</h3>
            <div class="author">作者1</div>
            <div class="date">11/01</div>
          </div>
          <div class="article a2">
            <h3 class="title t2">文章標題2</h3>
            <div class="author">作者2</div>
            <div class="date">11/02</div>
          </div>
          <div class="article a3">
            <h3 class="title t3">文章標題3</h3>
            <div class="author">作者3</div>
            <div class="date">11/03</div>
          </div>
        </div>
        <div id="footer">
          <p class="address">臺北市信義區</p>
          <p class="copyright">&copy; Copyright 2019</p>
        </div>
      </body>
    </html>
"""

if __name__ == "__main__":
    app.run()