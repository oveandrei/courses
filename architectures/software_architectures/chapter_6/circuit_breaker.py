
"""Circuit Breaker
Idea: Prevent repeated calls to a failing service
"""

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)

@breaker
def call_payment_service():
    return requests.post("http://payment-service/pay", timeout=2)

