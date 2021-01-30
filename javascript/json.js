'use strict';

//1.Object to JSON
//stringfy(obj)

let json = JSON.stringify(true)

json = JSON.stringify(["apple","banana"])

console.log(json);

const rabbit = {
    name: 'tori1',
    color: 'white',
    size: null,
    birthday: new Date(),
    jump: () => {
        console.log(`${this.name} can jump!`)
    }
};

json = JSON.stringify(rabbit);

console.log(json);
//함수는 데이터가 아니기때문에 JSON변경 되지않음
json = JSON.stringify(rabbit,['name','color']);
console.log(json);
console.clear();

json = JSON.stringify(rabbit,(key, value) => {
    console.log(`key : ${key} , value: ${value}`);
    return key === "name" ? "jc" : value;
});

console.log(json);


//2.JSON to Object
//parse(json)

console.clear();

const obj = JSON.parse(json,(key,value) =>{
    console.log(`key : ${key} , value: ${value}`);
    return key === "birthday" ? new Date(value) : value;
});

//console.log(obj);
//rabbit.jump();  //jump가 출력되지만 
//obj.jump();     //jump가 출력안된다

console.log(rabbit.birthday.getDate()); //실행됨
console.log(obj.birthday.getDate());    //에러
