import React, { useState } from 'react';
import axios from 'axios';
import './TaskForm.css'; 

function TaskForm({ fetchTasks, apiEndpoint }) {
  const [task, setTask] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!task) return;

    try {
      await axios.post(apiEndpoint, {
        task: task,
        completed: false,
      });
      setTask(''); // Clear the input field
      fetchTasks(); // Refresh the task list
    } catch (error) {
      console.error('Error creating task:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="task-form"> {/* Apply class for styling */}
      <input
        type="text"
        placeholder="Enter a new task"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <button type="submit">Add Task</button>
    </form>
  );
}

export default TaskForm;
