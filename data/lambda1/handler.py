import json

from aws_lambda_typing import context as lambda_context


def lambda_handler(event: dict, context: lambda_context.Context):
    """
    AWS Lambda handler function.

    Parameters:
    event (dict): Event data passed to the function.
    context (LambdaContext): Runtime information.

    Returns:
    dict: Response object.
    """
    # Log the received event
    print("Received event:", json.dumps(event, indent=2))

    # Process the event (example: return a greeting message)
    name = event.get("name", "World")
    message = f"Hello, {name}!"

    # Create the response object
    response = {"statusCode": 200, "body": json.dumps({"message": message})}

    return response
