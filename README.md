# Currency_Converter
The Currency convertion application was creates be backend Python and Flask, not Javascript.

I built a small currency converter. This was done using the forex-python module which was installed in my virtual environment using pip install forex-python.

The application has the following:

A form with three inputs:

One input to type in a three letter currency code to convert from
One input to type in a three letter currency code to convert to
Another input to type in a number amount to convert

I started by Setting up the Flask App and forex-python, 
then Proceeded to creating the routes, Ran the app, Creating Helper Functions (in utils.py):, 
Creating HTML Templates, and then writing Tests, test_app.py, 

Testing showed that $1 USD converted to $1 USD. This showed that the Flask app works, 
however, the API seems to be buggy because it doesn't convert other currencies properly
