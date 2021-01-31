'use strict';
window.onload = () => {};
document.getElementById('form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const name = e.target.userName.value;
  if (!name) {
    return alert('이름을 입력해주세요');
  }
  try {
    await axios.post('/user', { name });

    //const res = await axios.get('/users');
  } catch (err) {
    console.log(err);
  }
});
