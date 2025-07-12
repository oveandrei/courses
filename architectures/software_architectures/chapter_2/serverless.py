
"""lambda_function.py"""

# A simple lambda function
def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "World")
    return {
        "statusCode": 200,
        "body": f"Hello, {name}"
    }

"""
    Deployment steps
1. Zip the lambda_function.py
2. Upload to AWS Lambda
3. Configure an API Gateaway trigger
4. Test via: 
    GET https://{api-id}.execute-api.{region}.amazonaws.com/dev/?name=Alice
"""
