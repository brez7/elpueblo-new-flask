docker build -t elpumex .


docker run -p 5000:5000 elpumex

browser-sync start --proxy "http://127.0.0.1:5000" --files "static/*, templates/**/*.html"



 
 