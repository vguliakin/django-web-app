import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
        
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_todo_list(self):

        # User goes to the homepage of app
        self.browser.get("http://localhost:8000")

        # User notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # User is invited to enter to-do item straight away
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # User types "Buy peacock feathers" into a text box
        input_box.send_keys("Buy peacock feathers")

        # When user hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows),
                            "New to-do item did not appear in table",
                        )

        # There is still a text box inviting user to add another item.
        # User enters "Use peacock feathers to make a fly"
        self.fail("Finish the test!")
        # The page updates again, and now shows both items on user list

if __name__ == "__main__":
    unittest.main()