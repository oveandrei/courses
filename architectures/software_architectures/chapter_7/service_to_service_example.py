

"""Secure Service-to-Service Communication"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, ssl_certfile="cert.pem", ssl_keyfile="key.pem")

# ssl_certfile = "cert.pem" <- Enables HTTPS by providing a certificate file. This must be a valid certificate
# ssl_keyfile = "key.pem" <- The private key corresponding to the certificate. Used to encrypt/decrypt secure comm.