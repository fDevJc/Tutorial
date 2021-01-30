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

user //
  .loginUser("ellie", "dream")
  .then(user.getRoles)
  .then(console.log);
console.log(1);
