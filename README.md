# p2hacks_xmastree
created by U.N.E. and i544c

## What is this
Xmas Tree made by Tweets.
ツイッターのつぶやきを用いて作られたクリスマスツリー。

## Development
Write code👩‍💻 👨‍💻

Requirements
- Python3.7.5
- [pipenv](http://flask.palletsprojects.com/en/1.1.x/)
  - You can install by `pip install pipenv`

First, you have to install python libraries.
`pipenv install --dev`

Run the development server.
```sh
export FLASK_APP=app.py FLASK_ENV=development
pipenv run flask run`
```

Now, you can write code!

## Deploy
We use [Dokku](http://dokku.viewdocs.io/dokku/).

Frontend
```sh
cd view && yarn build
rsync -av view/build/ root@dokku.i544c.me:/var/lib/dokku/data/storage/xmastree/view/build/
ssh root@dokku.i544c.me chown -R 32767:32767 /var/lib/dokku/data/storage/xmastree/view/
```
