'use strict';
//Login form placeholders
try{
    const inputUser = document.querySelector('#id_username'),
          inputPassword = document.querySelector('#id_password');

          inputUser.setAttribute('placeholder', 'Логін');
          inputPassword.setAttribute('placeholder', 'Пароль');}catch{}


//Register form
const clearForm = () => {
    const formInput = document.querySelectorAll('input')
    formInput.forEach(elem=>{
        console.log(elem);
        elem.remove()})
}

try{
    const registerButton = document.querySelector('#registerButton'),
          registerForm = document.querySelector('#register');


    registerButton.addEventListener('submit', (event)=>{
        event.preventDefault();
        clearForm();

        let phoneNumberField = document.createElement('input'),
            smsCodeField = document.createElement('input');

        phoneNumberField.setAttribute('placeholder', 'Номер телефона');
        phoneNumberField.setAttribute('placeholder', 'SMS код');
        registerForm.insertAdjacentElement('afterend', phoneNumberField);
        registerForm.insertAdjacentElement('afterend', smsCodeField);
        })
    }catch{};
