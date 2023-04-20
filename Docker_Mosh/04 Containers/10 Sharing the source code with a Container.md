- Now that we have our container running
- Make some changes in the application, and you will observe that the changes are not reflected in the application

#### Publishing changes
- For Production machine: We should always build a new image, tag it and build it properly
- For development:
	- ~~Build a new image~~
	- ~~Copy files~~
- We can create a mapping or binding between a directory on the host and a directory inside the container, in this way any changes we make to the files inside this directory are immediately visible inside the container. 