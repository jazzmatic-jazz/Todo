## **PROJECT TITLE**
TO-DO

## **DESCRIPTION**
The Project APIs should allow users to create, update, delete and retrieve tasks. Each task can have a title, description, due_date and status.


## **Installation**

To install Project Title, follow these steps:
1. Clone the repository: **`git clone https://github.com/jazzmatic-jazz/Todo.git`**
2. Navigate to the project directory: **`cd todo`**
3. Install dependencies: **`pip install -r requirements.txt`**
4. Run Migrations: **`py manage.py makemigrations`**
5. Migrate: **`py manage.py migrate`**
6. Run the project: **`py manage.py runserver`**

## **API Endpoint**

1. Register user: **`api/register`**
2. Todo List: **`api/`**
3. Create Task: **`api/create`**
4. Task Detail: **`api/detail/<int:pk>`**
5. Update and Delete: **`api/up-del/<int:pk>`**

