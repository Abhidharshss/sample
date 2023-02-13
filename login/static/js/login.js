function login(x){
    var name = /^[A-Za-z ]+$/;

    if(x.username.value == ""){
        alert("Enter your username");
        x.username.focus();
        return false;
    }else if(!x.username.value.match(name)){
        alert("Invalid username");
        x.username.focus();
        return false;
    }
    if(x.password.value == ""){
        alert("Enter your password");
        x.password.focus();
        return false;
    }
}