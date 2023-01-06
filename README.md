# GoldenInfo
#### GoldenInfo is simple python script to automate dorcking search

Google Dorks are advanced search queries that are used to find specific information on the internet. They are often used to find specific websites or documents that may not be easily discoverable through a normal search. Google Dorks are formed by using special operators and commands in the Google search engine that allow users to search for specific types of information. They can be used to find websites that contain a specific type of content, are hosted on a specific type of server, or have a specific type of vulnerability. Some examples of Google Dorks include:

```
site:example.com - searches for pages on the domain example.com
intitle:"index of" - searches for pages with "index of" in the title
inurl:"login.php" - searches for pages with "login.php" in the URL
intext:"confidential" filetype:doc - searches for Microsoft Word documents that contain the word "confidential"
inurl:admin site:example.com - searches for pages on the domain example.com with "admin" in the URL
intext:"username" intext:"password" - searches for pages that contain both "username" and "password"
inurl:"viewerframe?mode=refresh" - searches for pages with "viewerframe?mode=refresh" in the URL
intext:"email" filetype:xls - searches for Microsoft Excel spreadsheets that contain the word "email"
intext:"private" intext:"key" filetype:pem - searches for files with the .pem extension that contain both "private" and "key"
```
### Examples
```
filetype:php inurl:catalog/admin/

inurl:group_concat(username, filetype:php intext:admin

intext:@gmail.com filetype:xls

intext:charset_test= email= default_persistent=

filetype:sql inurl:wp-content/backup-*

inurl:/wwwboard/passwd.txt

ext:pwd inurl:(service | authors | administrators | users) “# -FrontPage-”

inurl:config/databases.yml -trac -trunk -”Google Code” -source -repository

server-dbs “intitle:index of”

“inurl:Teamspeak2_RC2/server.log”

“admin account info” filetype:log

filetype:pem pem intext:private

intitle:”Index of..etc” passwd
```

Google Dorks can be very useful for finding specific types of information on the internet, but they can also be used for malicious purposes, such as locating vulnerable websites or sensitive documents that should not be publicly available. As a result, the use of Google Dorks is sometimes considered a gray area in terms of ethics.




