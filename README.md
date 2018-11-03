# cat-button
🐈 🍖 📢 #️⃣

Post a message to Slack when the cats have been fed.

## Development and deployment - macOS

All of this is terrible. We need to build a deployment package to get a usable environment with `slackclient` in AWS Lambda.

The lambda env needs Python 3.6 to work, but the latest version of Python 3 is 3.7 which is what brew provides.

To switch Python environments (from [Stack Overflow](https://stackoverflow.com/questions/51726203/installing-python3-6-alongside-python3-7-on-mac)) we need to run the following once to install Python 3.6.5:
```
brew unlink python
brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
```

Then to actually switch our Python version for local development:
```
brew switch python 3.6.5_1
```

**⚠️ Note switching this breaks almost everything else installed by brew, don't forget to switch back!**

Create a virtualenv if necessary with:
```
bash
virtualenv --python=python3.6 cat_button_venv
```

Install requirements:

```
source cat_button_venv/bin/activate
pip install -r requirements.txt
```

Then to create the `.zip` deployment package from the root of this repo run:
- `./package.fish`

Then upload the deployment package `cat_button.zip` to an AWS lambda function and create a `SLACK_API_TOKEN` environment variable with a token like `xoxp-xxxx-xxxx-xxxx-xxxx`.

**Finally to switch back to a generally working Python environment:**
```
brew switch python 3.7.0
```
