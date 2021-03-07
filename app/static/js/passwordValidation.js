let passwordField = document.getElementById('passwordField');
let warning = document.getElementsByClassName('warning')[0];

let confirmField = document.getElementById('confirmField');
let confirmWarning = document.getElementsByClassName('confirm-warning')[0];

passwordField.addEventListener('focus', function(){
    warning.style.display = 'block';
});

passwordField.addEventListener('focusout', function(){
    warning.style.display = 'none';
});

confirmField.addEventListener('focus', function(){
    confirmWarning.style.display = 'block';
});

confirmField.addEventListener('focusout', function(){
    confirmWarning.style.display = 'none';
});