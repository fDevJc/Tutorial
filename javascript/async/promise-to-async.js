class UserStorage {
  loginUser(id, password) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (
          (id === "ellie" && password === "dream") ||
          (id === "jc" && password === "jc")
        ) {
          resolve(id);
        } else {
          reject(new Error("not found"));
        }
      }, 2000);
    });
  }

  getRoles = (user) => {
    if (user === "ellie") {
      return new Promise((resolve, reject) => {
        setTimeout(() => resolve({ name: "ellie", role: "admin" }), 1000);
      });
    }
  };
}

const user = new UserStorage();

async function getUser(user) {
  const userId = await user.loginUser("ellie", "dream").then((id) => id);
  console.log(userId);
  const userRole = await user.getRoles(userId).then((obj) => obj);
  return userRole;
}

//console.log(getUser(user).name);

console.log(getUser(user).then(console.log));
