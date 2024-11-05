// Add client-side form validation
document.addEventListener('DOMContentLoaded', function() {
    // Phone number formatting
    const phoneInputs = document.querySelectorAll('input[name="phone_number"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            let x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
            e.target.value = !x[2] ? x[1] : `(${x[1]}) ${x[2]}${x[3] ? '-' + x[3] : ''}`;
        });
    });
});
