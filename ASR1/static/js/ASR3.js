const progress = localStorage.getItem('progress');

if (progress) {
    const modal = new bootstrap.Modal(document.getElementById('staticBackdrop'), {
        keyboard: false,
        backdrop: 'static'
    });
    modal.show();
    document.getElementById('continueProgressButton').addEventListener('click', () => {
        document.querySelectorAll('.form-control').forEach(input => {
            const value = localStorage.getItem(input.name);
            if (value) {
                input.value = value;
            }
        })
        modal.hide();
    })
    document.getElementById('resetProgressButton').addEventListener('click', () => {
        localStorage.clear();
        modal.hide();
    })
}

document.querySelectorAll('.form-control').forEach(input => {
    input.addEventListener('change', () => {
        localStorage.setItem('progress', 'true');
        localStorage.setItem(input.name, input.value);
    })
})
