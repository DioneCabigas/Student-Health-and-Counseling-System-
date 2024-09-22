const addSessionModal = document.getElementById('addSessionModal');
const assignCounselorModal = document.getElementById('assignCounselorModal');

const addSessionBtn = document.querySelector('.add-session-btn');
const assignCounselorBtn = document.querySelector('.assign-counselor-btn');

const closeModal = document.querySelector('.modal-header .close');
const closeAssignModal = document.querySelector('.modal-header .close-assign');

function openModal(modal) {
    modal.style.display = 'block';
}

function closeModalFunction(modal) {
    modal.style.display = 'none';
}

addSessionBtn.addEventListener('click', () => {
    openModal(addSessionModal);
});

assignCounselorBtn.addEventListener('click', () => {
    openModal(assignCounselorModal);
});

closeModal.addEventListener('click', () => {
    closeModalFunction(addSessionModal);
});

closeAssignModal.addEventListener('click', () => {
    closeModalFunction(assignCounselorModal);
});

window.addEventListener('click', (event) => {
    if (event.target === addSessionModal) {
        closeModalFunction(addSessionModal);
    }
    if (event.target === assignCounselorModal) {
        closeModalFunction(assignCounselorModal);
    }
});
