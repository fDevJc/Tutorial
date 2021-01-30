//async & await
//clear style of using promise :)

async function fetchUser() {
  return "ellie";
}

const user = fetchUser();
//console.log(user);

//2. await
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function getApple() {
  await delay(2000);
  return "apple";
}

async function getBanana() {
  await delay(1000);
  return "banana";
}

function getBananaPromise() {
  return delay(1000).then(() => "banana2");
}

function pickFruits() {
  return getApple().then((a) => {
    console.log("a : " + a);
    return getBanana().then((b) => {
      console.log("b ; " + b);
      return `${a} , ${b}`;
    });
  });
}

//console.log("pf :" + pickFruits().then(console.log));

async function asyncPickFruits() {
  const apple = await getApple();
  const banana = await getBanana();

  return `${apple} , ${banana}`;
}
//asyncPickFruits().then(console.log);
//위의 함수같은 경우 getApple에서 1초 딜레이 , getBanana에서 1초 딜레이 총 2초딜레이

//병렬화
async function parallelAsyncPickFruits() {
  const applePromise = getApple();
  const bananaPromise = getBanana();
  const apple = await applePromise;
  const banana = await bananaPromise;

  return `${apple} , ${banana}`;
}

//parallelAsyncPickFruits().then(console.log);

function pickAllFruits() {
  return Promise.all([getApple(), getBanana()]).then((fruits) => fruits.join());
}
//promise 배열을 보내면 결과를 배열로 줌

//pickAllFruits().then(console.log);

function pickOnlyOne() {
  return Promise.race([getApple(), getBanana()]);
}

pickOnlyOne().then(console.log);
