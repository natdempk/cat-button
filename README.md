# cat-button
🐈 🍖 📢 #️⃣

## Dev

All of this is terrible. We need to build a deployment package to get a usable environment in AWS Lambda.

Using `pipenv` we want a virtualenv local to the directory we are in so first set the following environment variable:
- `export PIPENV_VENV_IN_PROJECT=1`

The lambda env needs Python 3.6 to work, but the latest version of Python 3 is 3.7 which is what brew provides.

To switch (from [Stack Overflow](https://stackoverflow.com/questions/51726203/installing-python3-6-alongside-python3-7-on-mac)):
```
brew switch python 3.6.5_1
```

**⚠️ Note switching this breaks almost everything else installed by brew, don't forget to switch back!**

Create a virtualenv if necessary with
```
bash
virtualenv --python=python3.6 cat_button_venv
```

Install requirements.

Then to create the `.zip` deployment package run:
- `./package.fish`

Then upload the deployment package to AWS!

To switch back:
- `brew switch python 3.7.0`
