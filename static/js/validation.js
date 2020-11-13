function validateContact() {
    var regName = /^[a-zA-Z]+$/;
    var regEmail = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
    var regContact = /^[0-9]+$/;
    var first_name = document.getElementById('id_firstName').value;
    var last_name = document.getElementById('id_lastName').value;
    var email = document.getElementById('id_email').value;
    var contact = document.getElementById('id_contact').value;
    if (!regName.test(first_name)) {
        alert('Invalid first name');
        document.getElementById('id_firstName').focus();
        return false;
    } else if (!regName.test(last_name)) {
        alert('Invalid Last name');
        document.getElementById('id_lastName').focus();
        return false;
    } else if (!regEmail.test(email)) {
        alert('Invalid Email');
        document.getElementById('id_email').focus();
        return false;
    } else if (!regContact.test(contact)) {
        alert('Invalid Contact');
        document.getElementById('id_contact').focus();
        return false;
    } else {
        return true;
    }
}

function validateEnlist() {
    var regName = /^[a-zA-Z0-9_ ]+$/;
    var regReturn = /^[0-9]+$/;
    var product_name = document.getElementById('id_name').value;
    var expected_return = document.getElementById('id_expectedReturn').value;
    if (!regName.test(product_name)) {
        alert('Invalid product name');
        document.getElementById('id_name').focus();
        return false;
    } else if (!regReturn.test(expected_return)) {
        alert('Invalid input');
        document.getElementById('id_expectedReturn').focus();
        return false;
    } else {
        return true;
    }
}


function validateRegister() {
    var regName = /^[a-zA-Z]+$/;
    var regEmail = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
    var regContact = /^[0-9]+$/;
    var regUsername = /^[a-zA-Z0-9_\-\.]+$/;
    var regPassword = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    var first_name = document.getElementById('first_name').value;
    var last_name = document.getElementById('last_name').value;
    var user_name = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var contact = document.getElementById('contact').value;
    var password1 = document.getElementById('password1').value;
    var password2 = document.getElementById('password2').value;

    if (!regName.test(first_name)) {
        alert('Invalid first name');
        document.getElementById('first_name').focus();
        return false;
    } else if (!regName.test(last_name)) {
        alert('Invalid Last name');
        document.getElementById('last_name').focus();
        return false;
    } else if (!regEmail.test(email)) {
        alert('Invalid Email');
        document.getElementById('email').focus();
        return false;
    } else if (!regContact.test(contact)) {
        alert('Invalid Contact');
        document.getElementById('contact').focus();
        return false;
    } else if (!regUsername.test(user_name)) {
        alert('Invalid Username');
        document.getElementById('username').focus();
        return false;
    } else if (password1 != password2) {
        alert('Passwords not same');
        document.getElementById('password1').focus();
        return false;
    } else if (!regPassword.test(password1)) {
        alert('Invalid Password');
        document.getElementById('password1').focus();
        return false;
    } else {
        return true;
    }
}


