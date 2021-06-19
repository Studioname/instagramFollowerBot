from instaFollower import InstaFollower
import os

instagram_email = os.environ['INSTAGRAM_EMAIL']
instagram_password = os.environ['INSTAGRAM_PASSWORD']
similar_account = os.environ['SIMILAR_ACCOUNT']
CHROME_DRIVER_PATH = r"C:\Users\Conan\Development\chromedriver_win32\chromedriver.exe"


instaFollower = InstaFollower(driver_path=CHROME_DRIVER_PATH, instagram_email=instagram_email, instagram_password=instagram_password, similar_account=similar_account)

instaFollower.login()
followers = instaFollower.find_followers()
instaFollower.follow(followers)