import logging
import logging.config
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains




# Load logger
logging.config.fileConfig('./src/logger.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def add_to_cart(wd):
    '''
    Press the 'Add to cart' button if possible.
    Returns 'True' if the button was successfully pressed.
    Returns 'False' otherwise (e.g., button was not found).

    :param WebDriver wd: Selenium webdriver with page loaded.
    :return: true if successful, otherwise false
    :rtype: boolean
    '''

    # Find add to cart button
    add_to_cart_button = wd.find_elements_by_xpath(
        '//*[@class="ProductCartAndWishlist"]/div[@class="button-group"]/button[@class="Button variant-primary size-normal"]|'
        '//*[@class="ProductAddToCart"]/button[@class="Button variant-primary size-normal"]')
    # Press button
    if len(add_to_cart_button) == 1 and add_to_cart_button[0].text.lower() == 'add to cart':
        logger.info('Scrolling into view')
        wd.execute_script("arguments[0].scrollIntoView();", add_to_cart_button[0])
        logger.info('Clicking on Add to cart')
        wd.execute_script("arguments[0].click();", add_to_cart_button[0])
        
        
        

        
        


        # Wait for item to successfully add to cart
        try:
            logger.info('Waiting for the decrement element')
            element = WebDriverWait(wd, 20).until(wd.find_element_by_xpath(
                '//*[@class="ProductQuantity variant-undefined"]//button[@class="Button variant-primary size-normal decrement"]'))
            return True
        
        except:
            logger.error('Adding to cart failed as decrement element not found after click')

    # No button
    elif len(add_to_cart_button) == 0:
        logger.warn('No "Add to cart" button found')

    # Multiple buttons
    else:
        logger.warn('Multiple "Add to cart" buttons found')

    logger.error('Could not add item to cart')
    return False
