const taskNameInput = document.getElementById('task_name');
const taskDescritptionInput = document.getElementById('task-description');
const taskCategoryInput = document.getElementById('task-category');

const innerContainer2 = document.getElementsByClassName('inner-container-2')[0];
const innerContainer3 = document.getElementsByClassName('inner-container-3')[0];

const createTaskBtn = document.getElementById('create-task-btn');
const loadTasksBtn = document.getElementsByClassName('load-tasks')[0];

createTaskBtn.addEventListener('click', (e) => {
    e.preventDefault();

    const taskData = {
        'task_name': taskNameInput.value,
        'task_description': taskDescritptionInput.value,
        'category': taskCategoryInput.value
    }

    fetch(BASE_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(taskData)
    })
        .then(clearForm);
});

loadTasksBtn.addEventListener('click', () => {
    fetch(BASE_URL)
        .then(res => res.json())
        .then(body => {
            Object.values(body).forEach(task => innerContainer2.appendChild(renderTask(task)))
        });
})

function renderTask(task) {
    const subContainer = document.createElement('div');
    subContainer.className = 'subcontainer';

    const h3 = document.createElement('h3');
    h3.textContent = task.task_name;

    const h4 = document.createElement('h4');
    h4.textContent = task.task_description;

    const h4_2 = document.createElement('h4');
    h4_2.textContent = task.category;

    subContainer.appendChild(h3);
    subContainer.appendChild(h4);
    subContainer.appendChild(h4_2);

    return subContainer;
};

function clearForm() {
    taskNameInput.value = '';
    taskDescritptionInput.value = '';
    taskCategoryInput.value = '';
};