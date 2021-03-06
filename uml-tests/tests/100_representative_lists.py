from testing import *
from common_tests import mps_test

# ------------------------------------------------------------------------

# This uses the result of the common test to check that Diane
# Abbot (the first MP in this data set) is in the list.

run_page_test(mps_test,
              lambda t,o: 1 == len(o.soup.findAll( lambda tag: tag.name == "a" and tag.string and tag.string == "Diane Abbott" )),
              test_name="Diane Abbott in MPs page",
              test_short_name="mps-contains-diane-abbott")

# As a slightly different example of doing the same thing, define
# a function instead of using nested lambdas:

def link_from_mp_name(current_test,http_test,name):
    all_tags = http_test.soup.findAll( lambda tag: tag.name == "a" and tag.string and tag.string == name)
    current_test.log("All the tags with the matching name are: "+str(all_tags))
    return 1 == len(all_tags)

def at_least_n_links(current_test,http_test,parent_type,parent_class,min_number):
    all_links = http_test.soup.find(parent_type, parent_class).findAll('a')
    current_test.log("There are %s links in parent %s (class %s)" % (len(all_links), parent_type, parent_class))
    return len(all_links) >= min_number

run_page_test(mps_test,
              lambda t,o: link_from_mp_name(t,o,"Richard Younger-Ross"),
              test_name="Richard Younger-Ross in MPs page",
              test_short_name="mps-contains-richard-younger-ross")

# ------------------------------------------------------------------------

msps_test = run_http_test("/msps/",
                          test_name="Fetching basic MSPs page",
                          test_short_name="basic-MSPs")

run_page_test(msps_test,
              lambda t,o: link_from_mp_name(t,o,"Brian Adam"),
              test_name="Brian Adam in MSPs page",
              test_short_name="msps-contains-brian-adam")

run_page_test(msps_test,
              lambda t,o: link_from_mp_name(t,o,"John Wilson"),
              test_name="John Wilson in MSPs page",
              test_short_name="msps-contains-john-wilson")

# ------------------------------------------------------------------------

mlas_test = run_http_test("/mlas/",
                          test_name="Fetching basic MLAs page",
                          test_short_name="basic-MLAs")

run_page_test(mlas_test,
              lambda t,o: at_least_n_links(t,o,"table", "people", 200),
              test_name="At least 200 links in MLAs page",
              test_short_name="mlas-contains-at-least-200-links")

# ------------------------------------------------------------------------
