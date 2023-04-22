# Simple Login I
- This is a login page that is developed in Python's Flask Framework and a backend MySQL server.

![Screenshot from 2023-04-22 21-43-48](https://user-images.githubusercontent.com/70995581/233795277-3c16f901-c52c-465d-9e45-ccc2ead5adbb.png)
![Screenshot from 2023-04-22 21-44-19](https://user-images.githubusercontent.com/70995581/233795279-9e98f115-d594-417d-8c10-e26c2487901c.png)

- The application is configured with default mysql server credentials.
```
username="root"
password=""
db_name="mysql"
```
![Screenshot from 2023-04-22 21-48-02](https://user-images.githubusercontent.com/70995581/233795669-2e6a843c-bc54-4e5f-b3ce-ceccca25ae0e.png)
- To enable custom configuration:
```html
....
# Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mysql"
        )
....
```
