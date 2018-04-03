# Todo Lists Site
---

## Description of the project

In this project we are going to be creating a website for managing a todo list. However this time we're going to be doing it from a Test Driven Development (TDD) standpoint, meaning **you** are going to write the unit tests,and then the code that the tests check.

This project will be built across five assignments:
1) Ultra basic site that has a single list for everybody
2) Make the site able to handle multiple lists
3) Modify the site to use Django Forms to handle input validation
4) Enable deletion of items
5) User authentication & permissions

You are provided with the shell of assignment 1 located in the `todo` directory and will build from there, all the code for your unit tests and site is to be located within that directory. We provide tests to validate your unit tests in the directories `assignment_1` through `assignment_5`.

## Testing your tests
For example you can find the tests for assignment #1 in `assignment_1/tests`. You'll want to read these files as they have been commented showing what to name your tests as well as what your tests should be testing for, including links to relevant documentation.

Example:

```python
from todo.tests import test_views as views_tests

class HomePageTestsPass(views_tests.HomePageTest):
    @rmotr_tester(test_mode=PASS)
    def test_home_page_renders_using_template(self):
        """
        Checks to ensure the page for '/' renders the appropriate template
        See assertTemplateUsed: https://docs.djangoproject.com/en/2.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed
        """
        super(HomePageTestsPass, self).test_home_page_renders_using_template()
```
This indicates that it expects a test class named `HomePageTest` inside `todo/tests/test_views.py` (**IMPORTANT. DO NOT WRITE YOUR TESTS IN THE ASSIGNMENT_1 FOLDER**) with a test called `test_home_page_renders_using_template`
There is also the hint that you may want to look at the documentation for `assertTemplateUsed` as it may be helpful when writing this test.

To run the tests for a particular assignment (assignment 1 in this example):
```
py.test assignment_5/tests
```
The tests will check both that your test has a proper pass condition, but also that it fails properly when tested against code that should fail.

## Assignment 1
You are provided with template files for the initial HTML content of the site, you need to write tests for both *views* and *models* to handle rendering the home page using templates, and the ability to `POST` new todo items to the page. For the moment we are only concerned with the ability to post new items and display them. You do not have to worry about deleting/checking off items. Everything should be handled on the same page/view, there is only a single todo list shared by everybody that uses the site, yes this is impractical but we'll build upon it.

## Assignment 2
We are now going to transition from a single list to being able to handle multiple lists. This results in the creation of two new endpoints, `/lists/new` for the creation of new lists, and `/lists/<list id>/` for accessing an existing list. This means that our form on the home page will now have to `POST` to the `/lists/new` address, and rendering of lists will take place solely on the `/lists/<list id>/` address. As a result of this our Models will also need to be updated as our Item objects will need to now be associated with a List.

## Assignment 3
We now are capable of handling multiple lists, however we aren't currently doing any validation of user input. We are going to implement [Django Forms](https://docs.djangoproject.com/en/2.0/ref/forms/api/#bound-and-unbound-forms) to add some input validation to our site. We do not want to allow users to add blank items, or duplicate items. Django Forms will also alow us to specify error messages so we'll use the following error messages:
- Empty item: `Blank list items are not permitted`
- Duplicate item: `Duplicate list items are not permitted`

## Assignment 4
It's finally time to update the site to allow people to delete items. For this we introduce a new endpoint: `/lists/<list id>/item/<item id>/delete`

## Assignment 5
As our last step we are going to add user authentication controls to our site. We'll just be using [Django's built-in user auth system](https://docs.djangoproject.com/en/2.0/topics/auth/) to do all the heavy lifting regarding users. We are going to require users login to use our site so this is going to some moving around in our tests. The home page will now redirect to the login page for users not logged in, and to a user's list (creating it if it doesn't exist) if they are logged in. This means that we'll write new tests for the home page, and the existing tests will be modified and moved to test against the list view page. Also, since we'll automatically be creating a new list if it doesn't exist for authenticated users, we'll no longer need the new list endpoint, thus its tests will be either removed or modified and moved to the list view endpoint. Finally we'll also put in some access controls such that Items and Lists will belong to the usesr that create them, and other users will be unable to view or delete those items.