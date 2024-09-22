// Get modal elements
const addSessionModal = document.getElementById('addSessionModal');
const assignCounselorModal = document.getElementById('assignCounselorModal');

// Get the buttons that open the modals
const addSessionBtn = document.querySelector('.add-session-btn');
const assignCounselorBtn = document.querySelector('.assign-counselor-btn');

// Get the <span> elements that close the modals
const closeModal = document.querySelector('.modal-header .close');
const closeAssignModal = document.querySelector('.modal-header .close-assign');

// Function to open a modal
function openModal(modal) {
    modal.style.display = 'block';
}

// Function to close a modal
function closeModalFunction(modal) {
    modal.style.display = 'none';
}

// When the user clicks the add-session button, open the Add Session modal
addSessionBtn.addEventListener('click', () => {
    openModal(addSessionModal);
});

// When the user clicks the assign-counselor button, open the Assign Counselor modal
assignCounselorBtn.addEventListener('click', () => {
    openModal(assignCounselorModal);
});

// When the user clicks on the close (x), close the Add Session modal
closeModal.addEventListener('click', () => {
    closeModalFunction(addSessionModal);
});

// When the user clicks on the close (x), close the Assign Counselor modal
closeAssignModal.addEventListener('click', () => {
    closeModalFunction(assignCounselorModal);
});

// Close the modals if the user clicks outside of the modal content
window.addEventListener('click', (event) => {
    if (event.target === addSessionModal) {
        closeModalFunction(addSessionModal);
    }
    if (event.target === assignCounselorModal) {
        closeModalFunction(assignCounselorModal);
    }
});
