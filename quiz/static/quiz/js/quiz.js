document.addEventListener("DOMContentLoaded", function () {
  const startBtn = document.getElementById("start-btn");
  const userInfoDiv = document.getElementById("user-info");
  const quizForm = document.getElementById("quiz-form");

  startBtn.addEventListener("click", function () {
    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (name === "" || phone === "") {
      alert("Please enter your name and phone number to start the quiz!");
      return;
    }

    // Hide user info, show quiz
    userInfoDiv.style.display = "none";
    quizForm.style.display = "block";

    // Optional: dynamically add hidden inputs to send name and phone to Django
    const nameInput = document.createElement("input");
    nameInput.type = "hidden";
    nameInput.name = "name";
    nameInput.value = name;
    quizForm.appendChild(nameInput);

    const phoneInput = document.createElement("input");
    phoneInput.type = "hidden";
    phoneInput.name = "phone";
    phoneInput.value = phone;
    quizForm.appendChild(phoneInput);
  });
});
