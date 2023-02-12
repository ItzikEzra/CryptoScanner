from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pytube import YouTube

# Open the browser
service_obj = Service("C:\webdriver.exe")
driver = webdriver.Chrome(service=service_obj)


def rahul_web_site():
    # Get function will send a grt request to the given nane
    url_site = 'https://rahulshettyacademy.com/angularpractice/'
    driver.get(url_site)
    print("Page title is: ", driver.title)

    # Size play
    # driver.maximize_window()
    # sleep(5)
    # driver.minimize_window()
    # sleep(5)

    driver.find_element(By.NAME, 'name').send_keys("Itzik Ezra")
    # driver.find_element(By.NAME, 'email').send_keys("ItzikEzra11@gmail.com")
    driver.find_element(By.ID, 'exampleInputPassword1').send_keys("ItzikEzra11@gmail.com")
    driver.find_element(By.ID, 'exampleCheck1').click()
    # XPATH
    # driver.find_element(By.XPATH,'//tagname[@attribute='value'])
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    message = driver.find_element(By.CLASS_NAME, 'alert-success').text
    print(message)
    assert 'success' in message

    print(driver.current_url)
    # Close function will close the window finally
    driver.close()


def lotto_scrapeer(lottory_num):
    driver.get("https://www.pais.co.il/lotto/archive.aspx")
    sleep(5)

    driver.find_element(By.ID, 'searchByNumber').click()
    sleep(5)

    driver.find_element(By.NAME, 'fromNumber').send_keys(lottory_num)
    # sleep(5)
    driver.find_element(By.NAME, 'toNumber').send_keys(lottory_num)
    #  sleep(5)
    driver.find_element(By.XPATH, '//a[@class="archive_form_button num w-inline-block"]').click()
    sleep(5)
    li = driver.find_elements(By.XPATH, '//li[@class="loto_info_num archive"]')
    for e in li:
        print(e.text)


def youtube_scraper(link, by_type, attr):
    driver.get(link)
    sleep(1)
    playlist = driver.find_elements(by_type, attr)
    sleep(1)

    links = []
    for video in playlist:
        links.append(video.get_attribute("href"))
    return links


def youtube_downloader(link):
    video_url = link
    yt = YouTube(video_url)

    # Choose the highest quality video stream available
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Download the video to the desired directory
    stream.download(filename="D:\\devops\\sela_vidoes")

def youtube_downloader_site(link):
    driver.get('https://en.y2mate.is/157/')
    driver.find_element(By.ID,'txtUrl').send_keys(link)
    driver.find_element(By.CLASS_NAME,'start-btn').click()
    sleep(10)
    driver.find_element(By.CSS_SELECTOR,"td[button[type='submit']").click()
    
def not_common(list1, list2):
    return list(set(list1) - set(list2))

# rahul_web_site()
# lotto_scrapeer(3552)


