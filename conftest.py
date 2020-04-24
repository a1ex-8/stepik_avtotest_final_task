import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default="firefox",
					help="Choose browser: chrome or firefox")
	parser.addoption('--language', action='store', default="en",
					help="Choose language: en,fr,ru,...")

@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption("browser_name")
	language = request.config.getoption("language")
	browser = None
	if browser_name == "chrome":
		print("\nuse language", language)
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': language})
		browser = webdriver.Chrome(options=options)
		print("\nstart chrome browser for test..")
	elif browser_name == "firefox":
		print("\nuse language", language)
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", language)
		browser = webdriver.Firefox(firefox_profile=fp)
		print("\nstart firefox browser for test..")
	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")
	yield browser
	print("\nquit browser..")
	browser.quit()


	