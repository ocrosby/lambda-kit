import json

from aws_lambda_typing import context as lambda_context


def lambda_handler(event: dict, context: lambda_context.Context) -> dict[str, any]:
    """
    AWS Lambda handler function.

    :param event: The event data.
    :param context: The context object.
    """
    # Log the received event
    print("Received event:", json.dumps(event, indent=2))
    print("Received context:", vars(context))

    # Process the event (example: return a greeting message)
    name = event.get("name", "World")
    message = f"Hello, {name}!"

    body = {"message": message}

    # Create the response object
    response = {"statusCode": 200, "body": json.dumps(body)}

    # Log the response
    print("Sending response:", json.dumps(response, indent=2))

    return response
