from flask import request, jsonify
from flask import Blueprint
import time
from scrapy.crawler import CrawlerRunner
from crawler.crawler.spiders.crawl_spider import CouponSpider
import crochet

crochet.setup()
routes_blueprint = Blueprint('routes', __name__)
output_data = []
crawl_runner = CrawlerRunner()


@routes_blueprint.route('/spider', methods=['POST'])
def scrape():
    if request.method == 'POST':
        url_scrapy = request.form['url']
        scrape_with_crochet(url_scrapy)
        time.sleep(20)
        return jsonify(output_data)


@crochet.run_in_reactor
def scrape_with_crochet(baseURL):
    global output_data
    eventual = crawl_runner.crawl(CouponSpider, web_url=baseURL)
    # eventual.addBoth(lambda _: crochet.stop())
    eventual.addCallback(collect_output_data)
    return eventual


def collect_output_data(result):
    global output_data
    output_data = result

