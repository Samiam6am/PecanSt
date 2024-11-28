<?php
// Database connection details
$servername = "localhost";
$username = "root";
$password = '$hithead8996!'; // Your actual password with the added "!"
$dbname = "pecan_st_lending"; // Replace with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get data from the form
$name = $_POST["name"];
$email = $_POST["email"];
$phone = $_POST["phone"]
;

// SQL query to insert data
$sql = "INSERT INTO clients (name, email) VALUES ('$name', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

