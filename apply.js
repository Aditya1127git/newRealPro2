const applyForm = document.querySelector("#applyForm");

const name = document.querySelector("#name");
const enrollment = document.querySelector("#enrollment");
const course = document.querySelector("#course");
const rollNumber = document.querySelector("#rollNumber");

const message = document.querySelector("#message");

applyForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const studentData = {
        name: name.value,
        enrollment: enrollment.value,
        course: course.value,
        rollNumber: rollNumber.value
    };

    const response = await fetch("https://realworldproject-production.up.railway.app/apply", {
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

    } else {

        const error = await response.json();

        message.innerHTML = `
        <div class="alert alert-danger mt-3">
            ${error.message}
        </div>
        `;
    }

});