from swaglabs import SwagLabs

def test_open_swaglabs_url(browser):

    swaglabs = SwagLabs(browser)
    swaglabs.open_url()

    assert swaglabs.is_bot_image_visible()

def test_login_swaglabs(browser):

    swaglabs = SwagLabs(browser)
    swaglabs.open_url()

    swaglabs.fill_username("standard_user")
    swaglabs.fill_password("secret_sauce")
    swaglabs.login_to_swaglabs()

    assert swaglabs.is_peekicon_image_visible()