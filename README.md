# flask-cat-image
a flask website made by bard AI, bard.google.com
From bard:
Here are the steps on how to setup a Raspberry Pi Apache Web Server:

Install Apache
The first step is to install Apache on your Raspberry Pi. To do this, open a terminal window and type the following command:

Code snippet
```
sudo apt-get install apache2
```
This will install the Apache web server on your Raspberry Pi.

Configure Apache
Once Apache is installed, you need to configure it. To do this, open the Apache configuration file in a text editor. The file is located at    
```
/etc/apache2/apache2.conf.
```
In the Apache configuration file, you need to find the following line:

Code snippet
```
#ServerName localhost
```
Change the value of localhost to the IP address of your Raspberry Pi. You can find the IP address of your Raspberry Pi by typing the following command in a terminal window:

Code snippet
```
ifconfig
```
Use code with caution. Learn more
Once you have changed the value of localhost, save the Apache configuration file and restart Apache. To restart Apache, type the following command in a terminal window:

Code snippet
```
sudo service
apache2 restart
```
Use code with caution. Learn more
Create a test HTML file
Now that Apache is configured, you can create a test HTML file. To do this, open a text editor and create a new file called index.html. In the index.html file, type the following code:

Code snippet
```
<!DOCTYPE html>
<html>
<head>
<title>My First Web Page</title>
</head>
<body>
<h1>This is my first web page!</h1>
</body>
</html>
```
Use code with caution. Learn more
Save the index.html file in the /var/www/html directory.

Test your web server
Now that you have created a test HTML file, you can test your web server. To do this, open a web browser and type the IP address of your Raspberry Pi into the address bar. If everything is working correctly, you should see the test HTML file in your web browser.

Congratulations! You have successfully setup a Raspberry Pi Apache Web Server.


