wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip
driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
driver.get('http://instagram.com/kodlamasanati')
follow_button_XP = ("//button[text()='Following' or \
                                  text()='Requested' or \
                                  text()='Follow' or \
                                  text()='Follow Back' or \
                                  text()='Unblock']"
                        )

(ActionChains(driver)
        .move_to_element(follow_button_XP)
        .click()
	.perform())

http://jonathansoma.com/lede/algorithms-2017/servers/setting-up/

exit
systemctl restart gunicorn.service
