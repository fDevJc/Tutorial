"use strict";

//Promise is a JavaScript object for asynchronous operation.
// state: pending -> fulfilled or rejected
// Producer vs Consumer

//1. Producer
//when new Promise is created, the executor runs automatically.
const promise = new Promise((resolve, reject) => {
  //doing some heavy work(newtwork , read files)

  console.log("doing comthing....");
  setTimeout(() => {
    resolve("elie");
    //reject(new Error("no network"));
  }, 2000);
});

//2. Consumer: then, catch, finally
promise
  .then((value) => {
    console.log(value);
  })
  .catch((error) => {
    console.log(error);
  })
  .finally(() => {
    console.log("finally");
  });

//3. Promise chaining
const fetchNumber = new Promise((resolve, reject) => {
  setTimeout(() => resolve(1), 1000);
});

fetchNumber
  .then((num) => num * 2)
  .then((num) => num * 3)
  .then((num) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(num - 1), 1000);
    });
  })
  .then((num) => console.log(num));

//4. Error Handling
const getHen = () =>
  new Promise((resolve, recject) => {
    setTimeout(() => resolve("chicken"), 1000);
  });
const getEgg = (hen) =>
  new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error(`error !! ${hen} => egg`)), 1000);
  });
const cook = (egg) =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve(`${egg} => food`), 1000);
  });
/*
getHen()
  .then((hen) => getEgg(hen))
  .then((egg) => cook(egg))
  .then((food) => console.log(food));
*/
getHen() //
  .then(getEgg)
  .catch((error) => "bread")
  .then(cook)
  .then(console.log)
  .catch(console.log);
