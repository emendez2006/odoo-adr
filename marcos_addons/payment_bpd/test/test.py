__author__ = 'eneldoserrata'

import urllib2
import httplib
import json

# have to export the DER certify recived from azul to base64
# openssl x509 -inform der -in MYCERT.cer -out my_cert.crt
# I ended up solving this by concatenating
# the private key you use to generate crs with your converted cert
# cat my_key.key my_cert.crt > certify.pem
CERT = "cartone.pem"
URL =  "https://pruebas.azul.com.do/WebServices/JSON/default.aspx"


class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    """Class to allow a certificate to be uploaded
    by the client."""
    def __init__(self, cert):
        urllib2.HTTPSHandler.__init__(self)
        self.cert = cert

    def https_open(self, req):
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=10):
        return httplib.HTTPSConnection(host, cert_file=self.cert, timeout=timeout)

opener = urllib2.build_opener(HTTPSClientAuthHandler(cert=CERT))

tx_bpd_request = {"TrxType": "Sale",
                  "CustomerServicePhone": False,
                  "OrderNumber": "TESTO019",
                  "PosInputMode": "E-Commerce",
                  "AcquirerRefData": "1",
                  "Amount": 180045, # Monto con impuesto incluido
                  "Itbis": 32408, #Valor del ITBIS
                  "CardNumber": "4012000077777777",
                  "Store": "39036610012",
                  "Plan": "0",
                  "CurrencyPosCode": "$",
                  "Payments": "1",
                  "ECommerceUrl": "cartone.com.do",
                  "CVC": 201,
                  "Channel": "EC",
                  "Expiration": 201701}


request = urllib2.Request(URL)
request.add_header("Content-Type", "application/json")
request.add_header("Auth1", "marcos")
request.add_header("Auth2", "marcos")

request.add_data(json.dumps(tx_bpd_request))
request.method = lambda: "POST"
response = opener.open(request)
resp = json.loads(response.readline())

from pprint import pprint as pp
pp(resp)