def prettyfier(func, *args):
    funcname = func.__name__
    array = funcname.split("_")

    for word in range(0, len(array)):
        array[word] = array[word].upper()

    funcPrettyName = " ".join(array)
    print(funcPrettyName, *args)


def open_browser(browser_name):
    prettyfier(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    prettyfier(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    prettyfier(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="vk.com")
find_registration_button_on_login_page(page_url="vk.com", button_text="Зарегистрироваться")
