document.addEventListener('DOMContentLoaded', function () {
    const signupForm = document.getElementById('signupForm');
    const modal = document.getElementById('verificationModal');
    const closeModal = document.querySelector('.close');
    const verificationInput = document.getElementById('verificationInput');
    const submitVerification = document.getElementById('submitVerification');

    // Generer en tilfeldig verifikasjonskode
    function generateVerificationCode() {
        return Math.floor(100000 + Math.random() * 900000); // Genererer en 6-sifret kode
    }

    // Når skjemaet blir sendt (på trykk på Registrer deg)
    signupForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Forhindrer skjemaet fra å bli sendt på vanlig måte

        // Generer og vis verifikasjonskode
        const code = generateVerificationCode();
        console.log("Verifikasjonskode: " + code); // Kan brukes til serverbehandling om ønskelig

        // Vis modal for verifikasjonskode
        modal.style.display = "block";

        // Skjul modal etter 30 sekunder
        setTimeout(function () {
            modal.style.display = "none";
        }, 30000); // 30000 ms = 30 sekunder
    });

    // Lukk modal
    closeModal.addEventListener('click', function () {
        modal.style.display = "none";
    });

    // Når verifikasjonskoden er bekreftet
    submitVerification.addEventListener('click', function () {
        const enteredCode = verificationInput.value;
        // Du kan sjekke om den innskrevne koden stemmer med den genererte koden her
        alert("Verifikasjonskode bekreftet!");
        modal.style.display = "none"; // Lukk modal
    });
});
