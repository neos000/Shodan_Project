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

Before running the file, you must create a new instance of the class.

`x = Shodan('API KEY HERE')`

To scan a server you must use the 'scan_server()' method.

`x.scan_server('ENTER SERVER PRODUCT')`

