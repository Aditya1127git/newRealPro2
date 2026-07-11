require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");


const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));


mongoose.connect(process.env.MONGO_URI)
    .then(function () {
        console.log("MongoDB Connected");
    })
    .catch(function (err) {
        console.log(err);
    });


const studentSchema = new mongoose.Schema({
    name: String,
    registration: String,
    course: String,
    email: String,
    phone: String
});

const Student = mongoose.model("Student", studentSchema);


const student2 = new Student({
    name: "Rahul Kumar",
    registration: "VTU002",
    course: "Btech in Computer Science",
    email: "rahu23@gmail.com",
    phone:"9889838483"
});

const student3 = new Student({
    name: "Akash Rajput",
    registration: "VTU003",
    course: "Btech in Computer Science",
    email: "aakashrajp223@gmail.com",
    phone:"7874333929"
});

const student4 = new Student({
    name: "Sidharth sahoo",
    registration: "VTU004",
    course: "Btech in Computer Science",
    email: "sidhujajf223@gmail.com",
    phone:"5576738829"
});

const student5 = new Student({
    name: "aryan paul",
    registration: "VTU005",
    course: "Btech in Computer Science",
    email: "aryanpau@gmail.com",
    phone:"9079594934"
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
        registration: req.body.registration
    })
        .then(function (existingStudent) {

            if (existingStudent) {

                return res.status(400).json({
                    message: "Registration Already Exists"
                });

            }

            const student = new Student({

                name: req.body.name,
                registration: req.body.registration,
                course: req.body.course,
                email: req.body.email,
                phone: req.body.phone

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
    res.send("Welcome to VTU backend");
});

app.listen(port, function () {
    console.log("Server Started.....");
});