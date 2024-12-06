import React from 'react'; 
import TaskItem from './TaskItem';
import './TaskList.css';  // Import the CSS file for styling

function TaskList({ tasks, fetchTasks, apiEndpoint }) {
  return (
    <div className="task-list">
      {tasks.length === 0 ? (
        <p>No tasks available.</p>
      ) : (
        tasks.map((task) => (
          <TaskItem key={task.id} task={task} fetchTasks={fetchTasks} apiEndpoint={apiEndpoint} />
        ))
      )}
    </div>
  );
}

export default TaskList;
