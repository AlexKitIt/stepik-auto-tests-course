
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_basket(browser):
        print("start test")
        browser.get(link)
        but=browser.find_elements_by_class_name("btn-add-to-basket")
        assert len(but) > 0, "Нет такой кнопки"
        print("finish test")