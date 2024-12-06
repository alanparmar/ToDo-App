# ToDo-App
This is a full-stack To-Do List application built with React for the frontend and AWS (API Gateway, Lambda, DynamoDB) for the backend. 
The app allows users to create, update, delete, and manage their tasks efficiently.

# Features
  Add new tasks with a name and status.\
  Update task names and statuses (Completed/Incomplete).\
  Delete tasks.\
  Responsive design with an intuitive user interface.
  - Backend powered by AWS services:
    - DynamoDB: Task storage.
    - API Gateway: REST API endpoints.
    - Lambda: Serverless logic handling.

# Technologies Used
- Frontend
  - React: Component-based user interface.
  - Axios: API communication.
  - CSS: Custom styling for responsive design.
- Backend
  - AWS Lambda: Serverless function handling business logic.
  - AWS DynamoDB: NoSQL database to store tasks.
  - AWS API Gateway: RESTful API for frontend-backend communication.
  - Boto3: Python SDK for AWS integration.

# Frontend setup
Clone the repository:

### `git clone <repository-url>`
### `cd frontend`

Install dependencies:

### `npm install`

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.

# Backend setup
1. Set up DynamoDB table:
- Create a table named ToDoTable with id as the primary key.
- Add columns for task, completed, and createdAt.
  
2. Deploy Lambda Functions:
- Write Lambda functions for AddTask, GetTasks, UpdateTask, and DeleteTask.
- Use the provided code in this repository.

3. Configure API Gateway:
- Create REST API endpoints for each Lambda function:
- - POST /tasks (Add Task)
- - GET /tasks (Fetch All Tasks)
- - PUT /tasks/{id} (Update Task)
- - DELETE /tasks/{id} (Delete Task)
4. Enable CORS:

- Enable CORS for API Gateway to allow communication between the frontend and backend.
