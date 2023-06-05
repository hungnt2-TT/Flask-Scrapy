import os
from flask import Flask, Blueprint, render_template, request, jsonify
from flask import Blueprint
import time
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import crochet

from crawler.crawler.spiders.crawl_spider import CouponSpider

crochet.setup()

routes_blueprint = Blueprint('routes', __name__)
output_data = []
crawl_runner = CrawlerRunner()


@routes_blueprint.route('/spider', methods=['POST'])
def scrape():
    if request.method == 'POST':
        url_scrapy = request.form['url']
        scrape_with_crochet(url_scrapy)
        print("output_data: ", output_data)
        print("TEST")
        time.sleep(20)
        return jsonify(output_data)


@crochet.run_in_reactor
def scrape_with_crochet(baseURL):
    print("baseURL: ", baseURL)
    global output_data
    eventual = crawl_runner.crawl(CouponSpider, category=baseURL)
    print("eventual: ", eventual)
    # eventual.addBoth(lambda _: crochet.stop())
    eventual.addCallback(collect_output_data)
    return eventual


def collect_output_data(result):
    global output_data
    output_data = result

