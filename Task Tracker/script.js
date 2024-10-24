
let myobject = JSON.parse(localStorage.getItem("tasks")) || [];
let list = document.getElementById("container");

const taskInput = document.getElementById("taskInput");
const addButton = document.getElementById("addButton");

function createTaskElement(taskText) {
    const taskDiv = document.createElement("div");
    taskDiv.classList.add("task-div");
    
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    
    const label = document.createElement("label");
    label.innerText = taskText;

    const deleteButton = document.createElement("button");
    deleteButton.type = "button";
    deleteButton.textContent = "X";

    taskDiv.appendChild(checkbox);
    taskDiv.appendChild(label);
    taskDiv.appendChild(deleteButton);
    list.appendChild(taskDiv);

    list.insertBefore(taskDiv, list.firstChild);

    // Checkbox change event
    checkbox.addEventListener("change", function () {
        if (checkbox.checked) {
            label.style.textDecoration = "line-through";
            label.style.color = "grey";
        } else {
            label.style.textDecoration = "none";
            label.style.color = "";
        }
    });

    // Delete button 
    deleteButton.addEventListener("click", () => {
        list.removeChild(taskDiv); 
        myobject.splice(myobject.indexOf(taskText), 1); 
        updateLocalStorage();
    });
}

// Function to update localStorage
function updateLocalStorage() {
    localStorage.setItem("tasks", JSON.stringify(myobject));
}

// Initial rendering from localStorage
myobject.forEach(item => {
    createTaskElement(item);
});

// Add button click event
addButton.addEventListener("click", () => {
    const taskText = taskInput.value.trim(); 
    if (taskText) {
        myobject.push(taskText); 
        createTaskElement(taskText); 
        updateLocalStorage(); 
        taskInput.value = ''; 
       
    }
});
