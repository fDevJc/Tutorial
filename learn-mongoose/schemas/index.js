const mongoose = require('mongoose');

const connect = () => {
  if (process.env.NODE_ENV != 'production') {
    mongoose.set('debug', true);
  }
  const DB_USER = 'root';
  const DB_PASSWORD = encodeURIComponent('pass');
  mongoose.connect(
    `mongodb://{DB_USER}:{DB_PASSWORD}}@localhost:27017/admin`,
    {
      dbNmae: 'nodejs',
      useNewUrlParser: true,
      useCreateIndex: true,
    },
    (error) => {
      if (error) {
        console.log('error : ', error);
      } else {
        console.log('mongodb success');
      }
    }
  );
};
mongoose.connection.on('error', (error) => {
  console.error('mongo err:', error);
});
mongoose.connection.on('disconnected', () => {
  console.error('mongo disconnect');
  //connect();
});

module.exports = connect;
