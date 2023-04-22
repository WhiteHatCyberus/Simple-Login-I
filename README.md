# Simple Login I
- To begin, install the packages in `requirements.txt` using the `apt` package installer.
- The application is configured with default mysql server credentials.
```
username="root"
password=""
db_name="mysql"
```
![f3](https://user-images.githubusercontent.com/70995581/233795669-2e6a843c-bc54-4e5f-b3ce-ceccca25ae0e.png)
- To enable custom configuration, open `app.py` in your editor and change the entry values:
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

- Run `app.py`
```python3
sudo python3 app.py
```
![f1](https://user-images.githubusercontent.com/70995581/233795277-3c16f901-c52c-465d-9e45-ccc2ead5adbb.png)
- Open http://localhost:5000 in your browser.
![f2](https://user-images.githubusercontent.com/70995581/233795279-9e98f115-d594-417d-8c10-e26c2487901c.png)
