# Shodan Project.
Dependencies: Shodan.


# Information
Experimenting with the **Shodan API**. Grabbing web server data such as hostnames, ports and IPs from multiple hosting providers such as nginx, 
MySql and many more. This is just an experimentation and I don't expect to update this project consistently.

You will need a **Shodan API key**, this will allow you to send valid requests to the API. If you do not have a Shodan API key, you will need to
acquire one. Follow the instructions below.

**To create an account follow the instructions listed below.**
1. Create a Shodan account here: https://account.shodan.io/register
2. Verify your account.
3. Once you have verified your account, navigate to the home page and click 'show api key' which is located at the top right of the screen.


**Basic usage.**

Before running the file, your first argument must be your api key.

You may change two variables in the script, the 'server_list' array and the 'element_filters' array. 
The server_list array contains the web hosting providers you wish to scan and the element_filters array contains
the data you would like to retrieve. Please read the Shodan API documentation if you're given an error such as
a 'KeyError'.

`server_list = [
            '',
        ]`
        
`element_filters = [
            '',
        ]`
