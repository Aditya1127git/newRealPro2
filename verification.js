const searchBtn = document.querySelector("#searchBtn");
const registration = document.querySelector("#registration");
const result = document.querySelector("#result");

async function searchStudent() {

    const registrationNumber = registration.value;
    const response = await fetch(`http://localhost:5000/student/${registrationNumber}`);

    if (!response.ok) {
        result.innerHTML = `
        <div class="alert alert-danger mt-4">
            Student Not Found
        </div>
    `;
        return;
    }

    const data = await response.json();

    result.innerHTML = `
<div class="card shadow mt-4 mx-auto" style="max-width:500px;">
    <div class="card-body">

        <h5 class="text-success text-center mb-3">
            ✅ Student Verified
        </h5>

        <h3 class="text-center mb-3">${data.name}</h3>

        <hr>

        <p><b>Registration :</b> ${data.registration}</p>

        <p><b>Course :</b> ${data.course}</p>

        <p><b>Email :</b> ${data.email}</p>

        <p><b>Phone :</b> ${data.phone}</p>

    </div>
</div>
`;
}

searchBtn.addEventListener("click", searchStudent);

registration.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        searchStudent();
    }
});