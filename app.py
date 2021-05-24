import os
from flask import Flask, url_for, redirect, request
from flask import render_template
from flask_talisman import Talisman
application = Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
        '*.googleapis.com',
        '*.mailchimp.com',
        '*.gstatic.com',
        '*.google-analytics.com',
        '*.googletagmanager.com',
        '*.amazon.com',
        '*.amazonaws.com',
        '*.cloudflare.com',
        '*.callrail.com'
    ],
    'script-src': [
        '\'self\'',
        '*.googleapis.com',
        '*.mailchimp.com',
        '*.gstatic.com',
        '*.google-analytics.com',
        '*.googletagmanager.com',
        '*.amazon.com',
        '*.amazonaws.com',
        '*.cloudflare.com',
        '*.callrail.com',
        '*.list-manage.com',
        '\'unsafe-inline\'',
    ],
    'style-src': [
        '\'self\'',
        '*.googleapis.com',
        '*.mailchimp.com',
        '*.gstatic.com',
        '*.google-analytics.com',
        '*.googletagmanager.com',
        '*.amazon.com',
        '*.amazonaws.com',
        '*.cloudflare.com',
        '*.callrail.com',
        '\'unsafe-inline\'',
    ]
}

@application.route("/")
def index():
    return render_template("home.html")

@application.route("/Form-a-Delaware-LLC")
def form_llc():
    return render_template("/Form-a-Delaware-LLC/index.html")

@application.route("/Form-a-Delaware-Corporation")
def form_corp():
    return render_template("/Form-a-Delaware-Corporation/index.html")

@application.route("/Sitemap")
def sitemap():
    return render_template("sitemap.html")


if __name__ == '__main__':
    application.run(debug=True)
