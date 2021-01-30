'use strict';

//JavaScript is synchronous.
//Excute the code block by orger after hoisting.
//hoisting: var, function declaration 자동으로 맨위로 올라간다

//console.log(1);

//비동기적인
//setTimeout(() =>  console.log(2) ,1000);

//console.log(2);
//console.log(3);

//synchronous callback 즉각적인
function printImmediately(print){
    print();
}

printImmediately(()=> console.log(11));

//asynchronous callback 언제실행될지모르는
function printWithDelay(print,timeout){
    setTimeout(print, timeout);
}

printWithDelay(()=> console.log("async callback"),2000);




//Callback Hell Example

class UserStorage{
    loginUser(id,password,onSuccess,onError){
        setTimeout(()=>{
            if (
                (id === "ellie" && password === "dream") ||
                (id === "jc" && password === "jc")
            ){
                onSuccess(id);
            }else{
                onError(new Error("not found"));
            }
        },2000);
    }
    getRoles(user, onSuccess, onError){
        setTimeout(()=>{
            if (user === "ellie"){
                onSuccess({name : "ellie", role: "admin"});
            }else{
                onError(new Error("no access"));
            }
        },1000);
    }
}

const user = new UserStorage();


//읽기힘듬 이해힘듬

user.loginUser("ellie", "dream", (id) => {
    user.getRoles(id, (obj) => {
        console.log(`name:${obj.name} , role:${obj.role}`);
    }, (err) => {
        console.log(err);
    })
}, (err) => {
    console.log(err);
});