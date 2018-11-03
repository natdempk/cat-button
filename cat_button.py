import os
from slackclient import SlackClient

TEST_CHANNEL = "C7M386WN8"
HOLLAND_CHANNEL = "G8TU9CA92" 

def hander(event, context):
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    sc.api_call(
        "chat.postMessage",
        channel=TEST_CHANNEL,
        text=":milo: :luna: The cats have been fed!",
        as_user=False,
        username="CatBot"
    )

    if response["ok"]:
        return {
                'statusCode': 200
        }
    else:
        return {
                'statusCode':500,
                'body': json.dumps(response)
        }
