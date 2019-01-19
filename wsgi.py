from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    import pprint
    from apiclient.discovery import build
    import socket
            #make api call to googles urlTestingTools
    API_KEY = 'AIzaSyACKc0SQ80qbBwgVnJUaBq_XVrmRHr8Ymw'
    service = build('searchconsole', 'v1', developerKey=API_KEY)
    url = 'https://google.com'
    params = {
                'url':url,
                'requestScreenshot':True,
                }
    req = service.urlTestingTools().mobileFriendlyTest().run(body=params, x__xgafv=None)
    try:
        response = req.execute()
        if response['mobileFriendliness'] == 'MOBILE_FRIENDLY':
            return 'mobile friendly'
    except socket.timeout:
        return 'there appears to be a problem at the moment, please try again later'

if __name__ == "__main__":
    app.run()
