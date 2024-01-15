let signInButton = document.getElementById("btnSignIn");
let signUpButton = document.getElementById("btnSignUp");

signInButton.addEventListener("click", (e) => {
    e.preventDefault()
    location.href = "/accounts/login/"
})

signUpButton.addEventListener("click", (e) => {
    e.preventDefault()
    location.href = "/accounts/register/"
})