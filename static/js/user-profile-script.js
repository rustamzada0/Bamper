const menuBtn = document.querySelector("#bars");
const navbar = document.querySelector("#asideBar");

menuBtn.addEventListener("click", () => {
    navbar.style.left === "0px" || navbar.style.left === ""
        ? navbar.style.left = "-100%" :
        navbar.style.left = "0px";
})
//////////////////////////////////
const editButton = document.getElementById("edit-button");
const saveButton = document.getElementById("save-button");
const data = document.getElementById("data");
const editForm = document.getElementById("edit-form");
const inputUserNum1 = document.getElementById("inputUserNum1");
const inputUserNum2 = document.getElementById("inputUserNum2");
const inputUserNum3 = document.getElementById("inputUserNum3");
const inputUserNum4 = document.getElementById("inputUserNum4");
const inputUserNum5 = document.getElementById("inputUserNum5");
const inputUserNum6 = document.getElementById("inputUserNum6");
const inputUserNum7 = document.getElementById("inputUserNum7");
const inputUserNum8 = document.getElementById("inputUserNum8");
const inputUserNum9 = document.getElementById("inputUserNum9");
const inputUserNum10 = document.getElementById("inputUserNum10");

editButton.addEventListener("click", () => {

    editForm.style.display = "flex";
    data.style.display = "none";
    document.getElementById("newInputUserNum1").value = inputUserNum1.textContent;
    document.getElementById("newInputUserNum2").value = inputUserNum2.textContent;
    document.getElementById("newInputUserNum3").value = inputUserNum3.textContent;
    document.getElementById("newInputUserNum4").value = inputUserNum4.textContent;
    document.getElementById("newInputUserNum5").value = inputUserNum5.textContent;
    document.getElementById("newInputUserNum6").value = inputUserNum6.textContent;
    document.getElementById("newInputUserNum7").value = inputUserNum7.textContent;
    document.getElementById("newInputUserNum8").value = inputUserNum8.textContent;
    document.getElementById("newInputUserNum9").value = inputUserNum9.textContent;
    document.getElementById("newInputUserNum10").value = inputUserNum10.textContent;
});

saveButton.addEventListener("click", () => {
    inputUserNum1.textContent = document.getElementById("newInputUserNum1").value;
    inputUserNum2.textContent = document.getElementById("newInputUserNum2").value;
    inputUserNum3.textContent = document.getElementById("newInputUserNum3").value;
    inputUserNum4.textContent = document.getElementById("newInputUserNum4").value;
    inputUserNum5.textContent = document.getElementById("newInputUserNum5").value;
    inputUserNum6.textContent = document.getElementById("newInputUserNum6").value;
    inputUserNum7.textContent = document.getElementById("newInputUserNum7").value;
    inputUserNum8.textContent = document.getElementById("newInputUserNum8").value;
    inputUserNum9.textContent = document.getElementById("newInputUserNum9").value;
    inputUserNum10.textContent = document.getElementById("newInputUserNum10").value;

    data.style.display = "flex";
    editForm.style.display = "none";
});
///////////////////////////
const chooseImageButton = document.getElementById("choose-image-button");
const imageUpload = document.getElementById("image-upload");
const profileImage = document.getElementById("profile-image");

chooseImageButton.addEventListener("click", () => {
    imageUpload.click();
});

imageUpload.addEventListener("change", (event) => {
    const selectedImage = event.target.files[0];

    if (selectedImage) {
        const imageUrl = URL.createObjectURL(selectedImage);

        profileImage.src = imageUrl;
    }
});

