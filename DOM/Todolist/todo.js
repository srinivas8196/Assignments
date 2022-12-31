const form = document.getElementById("form");
const taskInput = document.getElementById("task");
const todoList = document.getElementById("todo-list");
const totalTasksSpan = document.getElementById("total-tasks");
const completedTasksSpan = document.getElementById("completed-tasks");

let totalTasks = 0;
let completedTasks = 0;

form.addEventListener("submit", event => {
  event.preventDefault();

  const task = taskInput.value;
  if (!task) return;

  totalTasks++;
  totalTasksSpan.textContent = totalTasks;

  const li = document.createElement("li");
  li.textContent = task;

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.addEventListener("change", () => {
    if (checkbox.checked) {
      completedTasks++;
      completedTasksSpan.textContent = completedTasks;
    } else {
      completedTasks--;
      completedTasksSpan.textContent = completedTasks;
    }
  });
  li.prepend(checkbox);

  const deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.addEventListener("click", () => {
    totalTasks--;
    totalTasksSpan.textContent = totalTasks;
    if (checkbox.checked) {
      completedTasks--;
      completedTasksSpan.textContent = completedTasks;
    }
    todoList.removeChild(li);
  });
  li.appendChild(deleteButton);

  todoList.appendChild(li);
  taskInput.value = "";
});
