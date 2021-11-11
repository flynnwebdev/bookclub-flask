# Bookclub Flask

Minimal Python/Flask implementation of (part of) the [Rails Bookclub app](https://github.com/flynnwebdev/bookclub-2021.2) I use to teach Rails concepts in FastTrack.

It only has 5 base dependencies - `Flask`, `SQLObject`, `psycopg2`, `python-dotenv` and `JSONPickle`. The last one is only needed if you want to serve a JSON API. I've used it on the Books index route.

## Roadmap

I plan to expand this in the future to include:

- Authors (and their relationship to Books)
- Authentication and authorization
- Image upload

## Pre-requisites

Python 3. I've not tested it on 2.x.

Dependencies are handled by `pipenv` using a `Pipfile`. If you don't have `pipenv` you'll need to install it first, then create and open a new environment with it:

```sh
pip3 install pipenv && pipenv shell
```

## Installation

Once you have `pipenv` set up, you can install all dependencies to the new environment with:

```sh
rm Pipfile.lock && pipenv install
```

Copy `.env.sample` and update it with your Postgres credentials:

```sh
cp .env.sample .env
```

Initially, you'll need to set up your database and tables:

```sh
python3 db.py
```

You can also use the above to reset the DB (i.e. drop the database and create it again from scratch)

## Seeding

If you want to seed the DB with some sample records:

```sh
python3 seeds.py
```

You can run this any time to clear the tables and re-seed them.

## Running

To run the Flask server, just run `app.py`:

```sh
python3 app.py
```

Then open `http://localhost:5000/books` in your browser.