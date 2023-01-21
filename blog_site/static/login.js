let loginLink = document.getElementById("login-link");
let registerLink= document.getElementById("register-link");

let loginForm = document.getElementById("login-form");
let registerForm = document.getElementById("register-form");

function openRegisterForm() {
  loginForm.style.display = "none";
  registerForm.style.display = "flex";
}

function openLoginForm() {
  registerForm.style.display = "none";
  loginForm.style.display = "flex";
}

loginLink.addEventListener("click", openLoginForm);

registerLink.addEventListener("click", openRegisterForm);