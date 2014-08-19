from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)

browser.open('http://ctools.umich.edu')

login_button = browser.select('#ctoolsLogin')[0]
browser.follow_link(login_button)
