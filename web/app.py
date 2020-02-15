from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Nombre(Resource):

    # Returns true if n is a prime number
    def check_prime(self, n):
        x = 2
        while(x < n):
            if n % x == 0:
                # Factor other then 1 or n, number is composite
                return False
            x = x +1
        # Number is prime, while loop terminated without finding factor
        return True

    # Finds the next prime after n
    def next_prime(self, n):
        val = n + 1
        while(True):
            # Check if val (n + 1) is a prime
            if self.check_prime(val):
                return val
            else:
                val = val + 1

    # Returns prime factors of n. Returns an empty list if n is prime.
    def get(self, nb):
        if nb is None:
            return 404
        n = int(nb)
        factor_list = []
        prime = 1
        next_p = self.next_prime(prime)
        while (next_p <= n):
            while n % next_p == 0:
                n = n / next_p
                factor_list.append(next_p)
            prime = next_p
            next_p = self.next_prime(prime)
        return {"Nombre" : nb,
        "Facteurs_premiers":factor_list}, 200




api.add_resource(Nombre, '/factors/<string:nb>') #http://127.0.0.1/factors/5

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
