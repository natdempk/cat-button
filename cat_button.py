import os
import random
from slackclient import SlackClient

TEST_CHANNEL = "C7M386WN8"
HOLLAND_CHANNEL = "G8TU9CA92" 

MILOS = [":milo:", ":milo_glare:"]
LUNAS = [":luna_wat:", ":luna_derp:", ":luna_cat:"]

def handler(event, context):
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    milo = random.choice(MILOS)
    luna = random.choice(LUNAS)

    response = sc.api_call(
        "chat.postMessage",
        channel=TEST_CHANNEL,
        text=f"{milo} {luna} The cats have been fed!",
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


if __name__ == "__main__":
    handler("test", "test")