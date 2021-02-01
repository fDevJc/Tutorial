async function getUser() {
  console.log('getUser()');
  const res = await axios.get('/users');
  const users = res.data;
  console.log(users);
  const divList = document.getElementById('divList');
  divList.innerHTML = '';
  Object.keys(users).map((key) => {
    //console.log(users[key].name);

    const userDiv = document.createElement('div');
    const span = document.createElement('span');
    span.textContent = users[key].name;

    userDiv.appendChild(span);
    divList.appendChild(userDiv);
  });
}
window.onload = getUser();

document.getElementById('form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = e.target.userName.value;
  if (!name) {
    alert('check name');
  }
  try {
    await axios.post('/user', { name });
    getUser();
  } catch (err) {
    console.log(err);
  }
  e.target.userName.value = '';
});
