from getpass import getpass
from re import findall
from robobrowser import RoboBrowser
from sys import argv


def get_webdav_urls(username, password):

    # log in

    browser = RoboBrowser(history=True)
    browser.open('http://ctools.umich.edu')
    browser.follow_link(browser.find(id='ctoolsLogin'))

    login_form = browser.get_form()
    login_form['login'].value = username
    login_form['password'].value = password
    browser.submit_form(login_form)

    # get the results

    browser.follow_link(browser.find(
        class_='toolMenuLink ',
        title='For creating, revising, and deleting course and project sites'
    ))
    browser.open(browser.find(class_='portletMainIframe').attrs['src'])

    results = []

    course_links = browser.select('#sitesForm td h4 a[target="_top"]')
    for course_link in course_links:

        if not course_link.attrs:
            continue
        href = course_link.attrs['href']
        if '~' in href:
            continue

        results.append(
            'https://ctools.umich.edu/dav' +
            findall('\/[^\/]+$', href)[0]
        )

    return results


if __name__ == '__main__':

    if len(argv) < 2:
        print 'Please specify an output file.'
        exit(1)

    username = raw_input('Uniqname: ')
    password = getpass()
    output_path = argv[1]

    webdav_urls = get_webdav_urls(username, password)
    output_file = open(output_path, 'w')
    for url in webdav_urls:
        print >> output_file, url
