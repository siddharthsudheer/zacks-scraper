from exporter import export
from scraper import scraperUniversal


def scrape_this_url(ticker, url_extension, table_id, tab_id_in_table, num_pages2crawl):
	print("{0:6}{1:6}{2}".format("  ~~> ", ticker, ": "), end="", flush=True)
	final_url = "https://www.zacks.com/stock/chart/" + ticker + url_extension
	eps_data, company_name = scraperUniversal(final_url, table_id, tab_id_in_table, num_pages2crawl)
	print("Done.")
	return (company_name, ticker, final_url, eps_data)


def get_eps_12months(tickers):
	eps_url = "/eps"
	table_id = "DataTables_Table_3"
	tab_id_in_table = "ui-id-6"
	num_pages2crawl = 4
	export_table_title = "12 Month EPS"
	print("{0}{1}{2}".format("Scraping ", export_table_title, " data for:"))
	eps_data_collection = [scrape_this_url(ticker, eps_url, table_id, tab_id_in_table, num_pages2crawl) for ticker in tickers]
	export(eps_data_collection, export_table_title)


def get_consensus_estimates(tickers):
	consensus_estimates_url = "/eps"
	table_id = "DataTables_Table_4"
	tab_id_in_table = "ui-id-7"
	num_pages2crawl = 10
	export_table_title = "Consensus Estimate"
	print("{0}{1}{2}".format("Scraping ", export_table_title, " data for:"))
	consensus_estimates_data_collection = [scrape_this_url(ticker, consensus_estimates_url, table_id, tab_id_in_table, num_pages2crawl) for ticker in tickers]
	export(consensus_estimates_data_collection, export_table_title)


def get_eps_surprise(tickers):
	eps_surprise_url = "/price-eps-surprise"
	table_id = "DataTables_Table_3"
	tab_id_in_table = "ui-id-6"
	num_pages2crawl = 10
	export_table_title = "EPS Surprise"
	print("{0}{1}{2}".format("Scraping ", export_table_title, " data for:"))
	eps_surprise_data_collection = [scrape_this_url(ticker, eps_surprise_url, table_id, tab_id_in_table, num_pages2crawl) for ticker in tickers]
	export(eps_surprise_data_collection, export_table_title)