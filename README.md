# DJANGO API built over HackerNews' API.

## Setup
1. Clone the project repo 
2. cd into the project directory 
3. Prepare a virtual env
4. run `pip install -r requirements.txt` to install all dependencies
5. run `python manage.py runserver` to start the server



## Endpoints
1. GET: `/api/items` returns all items in the database
2. POST: `/api/items` post data to the database. Fields include `by`, `title`, `text`, `url`, `type`
3. PUT: `/api/items/:id` updates Item `id`
4. DELETE: `/api/items/:id` deletes item  `id`