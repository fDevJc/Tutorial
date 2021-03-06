'use strict';

async function getUser() {
  console.log('getUser()');

  const res = await axios.get('/users');
  const users = res.data;
  console.log(users);

  const divList = document.getElementById('divList');
  divList.innerHTML = '';

  Object.keys(users).map((key) => {
    const userDiv = document.createElement('div');
    const span = document.createElement('span');
    span.textContent = users[key];
    const edit = document.createElement('button');
    edit.textContent = '수정';
    edit.addEventListener('click', async () => {
      //
    });
    const remove = document.createElement('button');
    remove.textContent = '삭제';
    remove.addEventListener('click', async () => {
      //
    });

    userDiv.appendChild(span);
    userDiv.appendChild(edit);
    userDiv.appendChild(remove);
    divList.appendChild(userDiv);
  });
}
window.onload = getUser();

document.getElementById('form').addEventListener('submit', async (e) => {
  e.preventDefault();
  //name setting
  try {
    const name = e.target.userName.value;
    if (!name) {
      alert('check name');
    }
    await axios.post('/user', { name });
    getUser();
  } catch (err) {
    console.log(err);
  }
  e.target.userName.value = '';
});
