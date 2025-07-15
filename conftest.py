import pytest, json
from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.options import Options

DEFAULT_WAIT_TIME = 7
SUPPORTED_BROWSERS = ['chrome', 'firefox']
CHROMEDRIVER_PATH = 'chromedriver'
FIREFOX_PATH = 'geckodriver'
CONFIG_PATH = 'config.json'

# Fixture 'scope="session"' provides just 1 run before X tests
@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain proper "browser". '
                        'Please modify "browser": "your_browser".')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        driver = Chrome(options=options)
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    # Return the driver object at the end of setup
    yield driver
    # For cleanup, quit the driver
    driver.quit()
