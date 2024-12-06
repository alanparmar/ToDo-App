import React, { useState } from 'react';
import axios from 'axios';
import './TaskItem.css';

function TaskItem({ task, fetchTasks, apiEndpoint }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editedTask, setEditedTask] = useState(task.task);
  const [editedStatus, setEditedStatus] = useState(task.completed);

  // Function to handle task deletion
  const deleteTask = async () => {
    try {
      await axios.delete(`${apiEndpoint}/${task.id}`);
      fetchTasks(); // Refresh the task list after deletion
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  // Function to handle task update
  const updateTask = async () => {
    try {
      await axios.put(`${apiEndpoint}/${task.id}`, {
        task: editedTask,
        completed: editedStatus,
      });
      setIsEditing(false); // Exit editing mode
      fetchTasks(); // Refresh the task list after updating
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  return (
    <div className="task-item">
      {isEditing ? (
        <>
          <input
            type="text"
            value={editedTask}
            onChange={(e) => setEditedTask(e.target.value)}
            className="edit-input"
          />
          <div className="status-toggle">
            <label>
              <input
                type="checkbox"
                checked={editedStatus}
                onChange={(e) => setEditedStatus(e.target.checked)}
              />
              Mark as {editedStatus ? 'Incomplete' : 'Completed'}
            </label>
          </div>
        </>
      ) : (
        <p>
          <strong>{task.task}</strong> - <span>{task.completed ? 'Completed' : 'Incomplete'}</span>
        </p>
      )}

      <div className="task-actions">
        {isEditing ? (
          <>
            <button onClick={updateTask} className="save-button">
              Save
            </button>
            <button onClick={() => setIsEditing(false)} className="cancel-button">
              Cancel
            </button>
          </>
        ) : (
          <>
            <button onClick={() => setIsEditing(true)} className="edit-button">
              Edit
            </button>
            <button onClick={deleteTask} className="delete-button">
              Delete
            </button>
          </>
        )}
      </div>
    </div>
  );
}

export default TaskItem;
