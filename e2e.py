from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
executable_path = "C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe"


def test_scores_service():
    openscorepage = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    openscorepage.get("http://localhost:8777/")
    scorefile = openscorepage.find_element_by_xpath("/html/body/main/div/div/h1/div").text
    score = int(scorefile)
    print(score)
    return 0 < score < 1000


def main_function():
    if test_scores_service():
        return exit(0)
    else:
        return exit(-1)


main_function()
