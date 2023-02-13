function register(x){
    var name = /^[A-Za-z ]+$/;
    var phone = /^[0-9]+$/;
    var mail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/


    if(x.firstname.value == ""){
        alert("Enter your first name");
        x.firstname.focus();
        return false;
    }else if(!x.firstname.value.match(name)){
        alert("Your first name contains invalid characters");
        x.firstname.focus();
        return false;
    }
    if(x.lastname.value == ""){
        alert("Enter your last name");
        x.lastname.focus();
        return false;
    }else if(!x.lastname.value.match(name)){
        alert("Your last name contains invalid characters");
        x.lastname.focus();
        return false;
    }
    if(x.email.value == ""){
        alert("Enter yout E-mail address");
        x.email.focus();
        return false;
    }else if(!x.email.value.match(mail)){
        alert("Invalid mail address");
        x.email.focus();
        return false;
    }
    if(x.phone.value == ""){
        alert("Enter your phone number");
        x.phone.focus();
        return false;
    }else if(!x.phone.value.match(phone)){
        alert("Your phone number contains invalid characters");
        x.phone.focus();
        return false;
    }else if(x.phone.value.length != 10){
        alert("Invalid phone number");
        x.phone.focus();
        return false;
    }else{
        var a=x.phone.value.split("");
        if(a[0]!=9 && a[0]!=8 && a[0]!=7 && a[0]!=6){
            alert("Invalid phone number");
            x.phone.focus();
            return false;
        }
    }
    if(x.address.value == ""){
        alert("Enter you address");
        x.address.focus();
        return false;
    }
}