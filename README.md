for University of Michigan students.

this scrapes all the WebDAV urls for your CTools Resources pages so you can download them. for the moment, it doesn't actually scrape the files, so you'll have to do it yourself. i'm lazy :(

get set up:

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

run it:

    python scrape.py
