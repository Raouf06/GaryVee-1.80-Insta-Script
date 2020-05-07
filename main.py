from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import random

class GaryVee:

	username = 'insta_user'
	password = 'insta_pass'

	tags = ['love', 'quote', 'motivation',
			'inspiration', 'life','quoteoftheday',
			'instagood', 'poetry', 'happy']

	comments = [
		'Your posts are amazing', 'Amazing work. Keep going!', 'Your photos are magnificent',
		'Your work fascinates me!', 'I like how you put your posts together', 'Great job',
		'What a really nice photo, great job!', 'Well done!', 'Your posts are amazing',
	]

	links = []

	total_cents_given = 0.0

	def __init__(self):
		self.browser = webdriver.Chrome(executable_path=r"C:/Users/Abderraouf/AppData/Local/Programs/Python/Python37/chromedriver.exe")
		self.login()

	def login(self):
		self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
		time.sleep(2)

		usernamefield = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
		usernamefield.send_keys(self.username)

		passwordfield = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
		passwordfield.send_keys(self.password)
		time.sleep(1)

		loginbutton = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
		loginbutton.click()
		time.sleep(3)

		self.get_links()

	def get_links(self):
		for i in self.tags:
			self.browser.get('https://www.instagram.com/explore/tags/' + i )
			time.sleep(2)

			links = self.browser.find_elements_by_tag_name('a')
			condition = lambda link: '.com/p/' in link.get_attribute('href')
			valid_links = list(filter(condition, links))

			for j in range(0, 9):
				link = valid_links[j].get_attribute('href')
				if link not in self.links:
					self.links.append(link)
		self.leave2cents()

	def leave2cents(self):
		for link in self.links:
			self.browser.get(link)
			time.sleep(1)

			self.comment()
			time.sleep(2)

			self.total_cents_given += 0.2

		print('You gave back $' + self.total_cents_given + ' to the community :) ' )

	def comment(self):
		comment_input = lambda: self.browser.find_element_by_tag_name('textarea')
		comment_input().click()
		comment_input().clear()

		comment = random.choice(self.comments)
		for letter in comment:
			comment_input().send_keys(letter)
			delay = random.randint(1, 3) / 30
			time.sleep(delay)

		comment_input().send_keys(Keys.RETURN)

		self.like()

	def like(self):
		like_button = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button')
		like_button.click()

		time.sleep(random.randint(3,7))

GaryVee()