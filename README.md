# CS50 Week 9 Lab 9

## [Implementation Details](https://cs50.harvard.edu/x/2021/labs/9/#implementation-details)
Complete the implementation of a web application to let users store and keep track of birthdays.

- [x] When the / route is requested via GET, your web application should display, in a table, all of the people in your database along with their birthdays.
- [x] First, in application.py, add logic in your GET request handling to query the birthdays.db database for all birthdays.
- [x] Pass all of that data to your index.html template.
- [x] Then, in index.html, add logic to render each birthday as a row in the table. - [x] Each row should have two columns: one column for the person’s name and another column for the person’s birthday.
- [x] When the / route is requested via POST, your web application should add a new birthday to your database and then re-render the index page.
- [x] First, in index.html, add an HTML form. The form should let users type in a name, a birthday month, and a birthday day. Be sure the form submits to / (its “action”) with a method of post.
- [x] Then, in application.py, add logic in your POST request handling to INSERT a new row into the birthdays table based on the data supplied by the user.
Optionally, you may also:

- [ ] Add the ability to delete and/or edit birthday entries.
- [x] Add any additional features of your choosing!
    _[Flask message flashing](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)_

### - [ ] Add the ability to delete and/or edit birthday entries.
- Change birthday records display into form
- User selects record(s) with checkbox
- User submits to delete
- application.py checks for matching record
- record is deleted