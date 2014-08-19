from robobrowser import RoboBrowser
import re


def get_webdav_urls(username, password):

    # log in

    browser = RoboBrowser(history=True)
    browser.open('http://ctools.umich.edu')
    browser.follow_link(browser.find(id='ctoolsLogin'))

    login_form = browser.get_form()
    login_form['login'].value = username
    login_form['password'].value = password
    browser.submit_form(login_form)

    # get the list of courses

    course_ids = []

    browser.follow_link(browser.find(
        class_='toolMenuLink ',
        title='For creating, revising, and deleting course and project sites'
    ))
    browser.open(browser.find(class_='portletMainIframe').attrs['src'])

    course_links = browser.select('#sitesForm td h4 a[target="_top"]')
    for course_link in course_links:
        if not course_link.attrs:
            continue
        href = course_link.attrs['href']
        if '~' in href:
            continue
        course_ids.append(re.findall('\/[^\/]+$', href)[0][1:])

    # get the webDAV url from every course

    results = []

    for course_id in course_ids:

        browser.open('https://ctools.umich.edu/portal/site/' + course_id)

        resources_link = browser.find(
            class_='toolMenuLink ',
            title='For posting documents, website URLs, etc.'
        )
        if not resources_link:
            continue
        browser.follow_link(resources_link)

        browser.open(browser.find(class_='portletMainIframe').attrs['src'])
        browser.follow_link(browser.find(
            title='Upload-Download Multiple Resources'
        ))

        url = browser.select('#davdocs_step1 p.indnt3 strong')[0].text
        results.append(url)

    return results


if __name__ == '__main__':

    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'

    webdav_urls = get_webdav_urls(username, password)
    print webdav_urls
