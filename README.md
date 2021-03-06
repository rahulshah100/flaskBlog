# flaskBlog
This a Blog created in Python-Flask.It is a multi-Page Website which has different pages for Home,About,Sample Posts,Contact.
It provides an admin panel where admin could add/edit/delete posts,files could be uploaded,background images could be changed.
This Admin panel is enabled with a login/logout facility.
Every Page inherits a same footer where Contact links of differenet social media handles are provided.
To make some parameter easily configurable,a config.json file is used to hold those specificities,like link for various social media handles,admin's password,username,number of posts to be displayed on a single page in Home Section,etc.
Slugs and Pagination techniques are used to fetch certain aforementioned number of posts on every different page.
Contact form has Flash notification system to acknowledge users that their data has been successfully sent.
Also an automatic mail update facility has been provided for admin,where as the contact form is subited,a mail including certain aforementioned details regarding the new entry would be sent to the admin.
For the briefing of the posts shown on Home page they could be clicked and further user could see the entire post on a different page.
