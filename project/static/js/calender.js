
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

let currentDate = new Date();

function renderCalendar() {
const currentMonthElement = document.getElementById("currentMonth");
const daysContainer = document.getElementById("daysContainer");
const currentMonth = currentDate.getMonth();
const currentYear = currentDate.getFullYear();

currentMonthElement.textContent = months[currentMonth] + " " + currentYear;

daysContainer.innerHTML = "";

const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);
const startDayOfWeek = firstDayOfMonth.getDay();
const totalDays = lastDayOfMonth.getDate();

  // Add day name abbreviations
for (let i = 0; i < dayNames.length; i++) {
    const dayNameElement = document.createElement("div");
    dayNameElement.textContent = dayNames[i];
    dayNameElement.classList.add("day", "day-name");
    daysContainer.appendChild(dayNameElement);
}

for (let i = 0; i < startDayOfWeek; i++) {
    const emptyDay = document.createElement("div");
    emptyDay.classList.add("day");
    daysContainer.appendChild(emptyDay);
}

for (let day = 1; day <= totalDays; day++) {
    const dayElement = document.createElement("div");
    dayElement.textContent = day;
    dayElement.classList.add("day");
    dayElement.addEventListener("click", () => {
    openModal(currentYear + "-" + (currentMonth + 1).toString().padStart(2, '0') + "-" + day.toString().padStart(2, '0'));
    });

    // Adding 6 appointment slots for each day
    for (let i = 0; i < 6; i++) {
    const appointmentSlot = document.createElement("div");
    appointmentSlot.classList.add("appointment-slot");
    dayElement.appendChild(appointmentSlot);
    }

    daysContainer.appendChild(dayElement);
}
}
function prevMonth() {
currentDate.setMonth(currentDate.getMonth() - 1);
renderCalendar();
attachEventListeners()
}

function nextMonth() {
currentDate.setMonth(currentDate.getMonth() + 1);
renderCalendar();
attachEventListeners()
}
// Initial render and click listeners setup
renderCalendar();
attachEventListeners()

function renderAppointments(dayElement) {
    const dayNumber = parseInt(dayElement.textContent);
    if (isNaN(dayNumber)) {
        return;
    }
    const appointmentsList = document.getElementById('appointmentsList');
    appointmentsList.innerHTML = '';
    const appointmentContainer = document.createElement('div');
    appointmentContainer.classList.add('appointment-container');
    for (let i = 10; i <= 18; i++) {
        const appointment = document.createElement('button');
        appointment.textContent = `${i}:00`;
        checkAppointmentExists(dayNumber, i, appointment);
        appointmentContainer.appendChild(appointment);

        // Update the click event listener for each appointment button
        appointment.addEventListener('click', function () {
            const selectedDate = dayElement.textContent;
            const selectedTime = `${i}:00`;
            redirectToAppointmentDetails(selectedDate, selectedTime);
        });
    }
    appointmentsList.appendChild(appointmentContainer);
}
function checkAppointmentExists(day, time, appointmentButton) {
    const currentMonth = currentDate.getMonth();
    const monthName = months[currentMonth];
    const xhr = new XMLHttpRequest();
    const url = `check_appointment/?date=${day}&time=${time}&month=${monthName}`;
    xhr.open('GET', url);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            const appointmentExists = JSON.parse(xhr.responseText).exists;
            if (appointmentExists) {
                appointmentButton.style.display = 'none';
            }
        }
    };
    xhr.send();
}
function redirectToAppointmentDetails(date, time) {
    const currentMonth = currentDate.getMonth();
    const monthName = months[currentMonth];
    const xhr = new XMLHttpRequest();
    const url = `details_booking/?date=${date}&time=${time}&month=${monthName}`;
    xhr.open('GET', url);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            window.location.href = url;
        }
    };
    xhr.send();
}
function attachEventListeners() {
    const days = document.querySelectorAll('.day');
    days.forEach(day => {
    day.addEventListener('click', function () {
        renderAppointments(this);
    });
    });
}  