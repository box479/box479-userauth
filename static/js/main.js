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

    // Profile picture preview
    const profilePicInput = document.querySelector('input[name="profile_picture"]');
    if (profilePicInput) {
        profilePicInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                if (!['image/jpeg', 'image/png', 'image/gif'].includes(file.type)) {
                    alert('Please select a valid image file (JPEG, PNG, or GIF)');
                    e.target.value = '';
                } else if (file.size > 5 * 1024 * 1024) {
                    alert('File size must be less than 5MB');
                    e.target.value = '';
                }
            }
        });
    }
});
