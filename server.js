
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");


const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(__dirname));


mongoose.connect(process.env.MONGODB_URI)
.then(() => {
    console.log("✅ MongoDB Connected");
})
.catch((err) => {
    console.log(err);
});


const studentSchema = new mongoose.Schema({
    studentId: String,
    name: String,
    registration: String,
    course: String,

    rollNumber: String,
    enrollmentNumber: String,
    academicSession: String,

    specialization: String,
    status: String,


});

const Student = mongoose.model("Student", studentSchema);


const student2 = new Student({
    studentId: "103840",
    name: "Rahul Kumar",
    registration: "NTI002",
    course: "Bachelor of Technology",
    specialization: "Computer Science",
    dualSpecialization: "NA",
    status: "RESULT PASS",
    email: "rahul@gmail.com",
    phone: "9876543210"
});

const student3 = new Student({
    name: "Akash Rajput",
    registration: "NTI003",
    course: "Btech in Computer Science",
    email: "aakashrajp223@gmail.com",
    phone: "7874333929"
});

const student4 = new Student({
    name: "Sidharth sahoo",
    registration: "NTI004",
    course: "Btech in Computer Science",
    email: "sidhujajf223@gmail.com",
    phone: "5576738829"
});

const student5 = new Student({
    name: "aryan paul",
    registration: "NTI005",
    course: "Btech in Computer Science",
    email: "aryanpau@gmail.com",
    phone: "9079594934"
});

// Student.insertMany([
//     student1,
//     student2,
//     student3,
//     student4,
//     student5
// ])
// .then(function () {
//     console.log("All Students Saved");
// })
// .catch(function (err) {
//     console.log(err);
// });

app.get("/students", function (req, res) {
    Student.find({})
        .then(function (data) {
            res.send(data);
        });
});

app.get("/student/:registration", function (req, res) {

    Student.findOne({
        registration: req.params.registration
    })
        .then(function (student) {

            if (student) {
                res.json(student);
            } else {
                res.status(404).json({
                    message: "Student Not Found"
                });
            }

        })
        .catch(function (err) {
            console.log(err);
            res.status(500).json({
                message: "Server Error"
            });
        });

});

app.post("/apply", function (req, res) {

    Student.findOne({
       registration: req.body.enrollment
    })
        .then(function (existingStudent) {

            if (existingStudent) {

                return res.status(400).json({
                    message: "Registration Already Exists"
                });

            }

            const student = new Student({

                
                rollNumber: req.body.rollNumber,

                studentId: "NTI" + Math.floor(1000 + Math.random() * 9000),

                enrollmentNumber: req.body.enrollment,

                academicSession: req.body.academicSession,
                name: req.body.name,
                registration: req.body.enrollment,
                course: req.body.course,

                specialization: "Computer Science",
                status: "RESULT PASS",

            });

            student.save()
                .then(function () {

                    res.send("Application Submitted");

                })
                .catch(function (err) {

                    res.status(500).send(err);

                });

        });

});

app.get("/", function (req, res) {
    res.send("Welcome to NTI backend");
});

app.listen(port, function () {
    console.log("Server Started.....");
});