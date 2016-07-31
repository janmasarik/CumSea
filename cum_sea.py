import dryscrape
import sys
from os import linesep
import lxml
import lxml.html
from traceback import format_exc
from threading import Thread


class SearchResult:
    def __init__(self, title, url, body):
        self.title = title
        self.url = url
        self.body = body

    def __eq__(self, other):
        return self.url == other.url

    def __str__(self):
        return "Title: " + self.title + linesep + "Url: " + self.url + linesep + "Description: " + self.desc

    def __hash__(self):
        return hash(self.url)


class CumSea:
    def __init__(self,search_term):
        self.search_term = search_term
        self.results = dict()

    def _get_result_page(self, base_url, search_xpath='//*[@name="q"]'):
        """
        loads result page using dryscrape
        :param base_url: url of search engine
        :param search_xpath: xpath of search form input field
        :return: lxml.html with search results
        """
        # if 'linux' in sys.platform:
        #     # start xvfb in case no X is running. Make sure xvfb
        #     # is installed, otherwise this won't work!
        #     dryscrape.start_xvfb()

        # set up a web scraping session
        sess = dryscrape.Session(base_url=base_url)

        # we don't need images
        sess.set_attribute('auto_load_images', False)

        # visit homepage and search for a term
        sess.visit('/')
        q = sess.at_xpath(search_xpath)
        q.set(self.search_term)
        q.form().submit()

        # dryscrape xpath processing sucks
        return lxml.html.fromstring(sess.body())

    def _google_search(self):

        html = self._get_result_page('http://google.com')
        search_results = html.xpath('//*[@id="ires"]/ol/div[@class="g"]')

        results = list()
        # extract first page results
        for result in search_results:
            try:
                results.append(SearchResult(
                    result.xpath('.//h3/a')[0].text_content(),
                    result.xpath('.//cite')[0].text_content(),
                    result.xpath('.//span[@class="st"]')[0].text_content(),))
            except IndexError as e:
                print 'Tried to load image, or some unexpected error occured: ', format_exc(e)

        self.results.update({
            'google': results
        })

    def _bing_search(self):

        html = self._get_result_page('http://bing.com')
        search_results = html.xpath('//*[@id="b_results"]/li[@class="b_algo"]')

        results = list()
        # extract first page results
        for result in search_results:
            try:
                results.append(SearchResult(
                    result.xpath('.//h2/a')[0].text_content(),
                    result.xpath('.//cite')[0].text_content(),
                    result.xpath('.//div[@class="b_caption"]//p')[0].text_content(),))
            except IndexError as e:
                print 'Tried to load image, or some unexpected error occured: ', format_exc(e)

        self.results.update({
            'bing': results
        })

    def cum_search(self):
        threads = []
        threads.append(Thread(target=self._google_search()))
        threads.append(Thread(target=self._bing_search()))
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
        self.results = zip(self.results['google'], self.results['bing'])
        return self.results

if __name__ == "__main__":
    c = CumSea("pokemonGo sux")
    c.cum_search()
