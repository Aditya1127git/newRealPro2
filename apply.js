const applyForm = document.querySelector("#applyForm");

const name = document.querySelector("#name");
const registration = document.querySelector("#registration");
const course = document.querySelector("#course");
const email = document.querySelector("#email");
const phone = document.querySelector("#phone");

const message = document.querySelector("#message");


applyForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const studentData = {
        name: name.value,
        registration: registration.value,
        course: course.value,
        email: email.value,
        phone: phone.value
    };


    const response = await fetch("http://localhost:5000/apply", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(studentData)
    });
    if (response.ok) {

        message.innerHTML = `
        <div class="alert alert-success mt-3">
            Application Submitted Successfully
        </div>
    `;

        applyForm.reset();

    }
    else {

        const error = await response.json();

        message.innerHTML = `
        <div class="alert alert-danger mt-3">
            ${error.message}
        </div>
    `;

    }

});