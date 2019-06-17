from selenium import webdriver


# Create chrome instance
#driver = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver")
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.find_element_by_id("pt-createaccount").click()
driver.find_element_by_id("pt-login").click()

# Set your query
driver.find_element_by_id("searchInput").send_keys("Design patterns")
driver.find_element_by_id("searchButton").click()

# get the text for the main sections of the article
heading = driver.find_element_by_id("firstHeading").text
see_also = driver.find_element_by_id("See_also").text
# domain_articles = driver.find_element_by_id("Domain-specific_articles").text
reading = driver.find_element_by_id("Further_reading").text
ref = driver.find_element_by_id("References").text
external_links = driver.find_element_by_id("External_links").text


def check_text(text_id, expected):
    if text_id == expected:
        print("Test passed!")
    else:
        print("Failed: Actual value", text_id, "Expected value", expected)


# Check the text for some items from our list
check_text(heading, "Design pattern")
check_text(see_also, "See also")
# check_text(domain_articles, "Domain-specific articles")
check_text(reading, "Reading")
check_text(ref, "References")
check_text(external_links, "External links")

# close page
driver.quit()