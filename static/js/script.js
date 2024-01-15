var toggleButton = document.getElementById("toggleButton");
        var textContainer = document.getElementById("textContainer");
        var inputContainer = document.getElementById("inputContainer");
        var isOpen = false;

        toggleButton.addEventListener("click", function() {
            isOpen = !isOpen; 

            if (isOpen) {
                toggleButton.textContent = "İmtina";
                textContainer.classList.add("hidden");
                inputContainer.classList.remove("hidden");
            } else {
                toggleButton.textContent = "Filterlə daxil edin";
                textContainer.classList.remove("hidden");
                inputContainer.classList.add("hidden");
            }
        });