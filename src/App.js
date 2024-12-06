import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TaskList from './TaskList';
import TaskForm from './TaskForm';
import './App.css'; 

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  const apiEndpoint = 'https://q2umknx9u4.execute-api.us-east-1.amazonaws.com/dev/tasks';

  // Fetch tasks from the backend
  const fetchTasks = async () => {
    try {
      const response = await axios.get(apiEndpoint, { headers: {
        'Content-Type': 'application/json',
      }}
);
      setTasks(response.data);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="App">
      <h1>To-Do List</h1>
      <TaskForm fetchTasks={fetchTasks} apiEndpoint={apiEndpoint} />
      {loading ? <p>Loading...</p> : <TaskList tasks={tasks} fetchTasks={fetchTasks} apiEndpoint={apiEndpoint} />}
    </div>
  );
}

export default App;
