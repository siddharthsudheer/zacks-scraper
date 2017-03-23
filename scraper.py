# from pyvirtualdisplay import Display
from contextlib import closing
from selenium.webdriver import Firefox



def scraperUniversal(url_src, table_id, tab_id_in_table, num_pages2crawl):

	# display = Display(visible=0, size=(800, 600))
	# display.start()

	with closing(Firefox()) as driver:
		driver.get(url_src)
		driver.implicitly_wait(5)

		table_tab = driver.find_element_by_id(tab_id_in_table)  # Required tab's ID from table
		table_tab.click()

		company_name = driver.find_element_by_xpath("//section[@id='quote_ribbon_v2']/header/h1/a").text
		data = []
		pageNum = 1
		while pageNum<=num_pages2crawl:
			for tr in driver.find_elements_by_xpath("//table[@id='" + table_id + "']//tr"):
				tds = tr.find_elements_by_tag_name("td")
				if tds:
					data.append([td.text for td in tds])
			driver.implicitly_wait(1)
			next_btn = driver.find_element_by_id(table_id + "_next")
			next_btn.click()
			pageNum += 1

	driver.quit()
	return (data, company_name)
