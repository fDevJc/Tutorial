const express = require('express');
const morgan = require('morgan');
const cookieParser = require('cookie-parse');
const session = require('express-session');
const dotenv = require('dotenv');
const path = require('path');

dotenv.config();
const app = express();

//아래 미들웨어들은 내부에 next를 호출하고 있으므로 연달아 쓸수있다.
//미들웨어 장착순서에 따라 어떤 미들웨어는 실행 되지 않을 수도 있다. (ex 정적 페이지를 리턴하는 미들웨어 다음)
//미들웨어간 데이터를 넘기고 싶다면 session에도 가능하지만 계속 유지된다는 단점이 있다.
//각 요청에 데이터를 저장하고 싶다면 req 객채에 데이터를 넣어두면된다.
/* 미들웨어를 사용하는 패턴
app.use(morgan('dev'));

app.use((req,res,next)=>{
    morgan('dev')(req,res,next);
})
해당방법을 사용하여 미들웨어의 기능을 확장할수 있다.(ex 환경변수에 따라 분기)
*/

//app.set()을 이용하여 값을 저장할수 있다
app.set('port', process.env.PORT || 3000);
//로그를 좀더 자세하게 보여주는 모듈
app.use(morgan('dev'));
//스태틱 미들웨어는 정적인 파일들을 제공하는 라우터 역할
//함수의 인수로 정적 파일들이 담겨 있는 폴더를 지정하면된다.
app.use('/', express.static(path.join(__dirname, 'public')));

//body-parser 본문에 있는 데이터를 해석해서 req.body로 만들어주는 미들웨어
//단 멀티파트 데이터는 처리못한다
// JSON과 url-encoded형식의 데이터이외에 Raw, Text형식의 데이터를 해석해야 할떄는 body-parser 모듈을 따로 설치해야한다.
//스트림 처리가 따로 필요없다 (ex. req.on('data'), req.on('end'))
//--아래 두 미들웨어--
//json형식을 해석
app.use(express.json());
//extended 옵션이 false이면 노드의 querystring 모듈을 사용하여 쿼리스트링을 해석 true이면 qs모튤을 사용하여 해석
//url주소형식을 해석
app.use(express.urlencoded({ extended: false }));

//인수로 비밀키를 받는다
//서명된 쿠키가 있는 경우 , 제공한 비밀 키를 통해 해당 쿠키가 내 서버가 만든 쿠키임을 검증할 수 있다.
//서명된 쿠키는 req.cookies 대신 req.signedCookies객체가 들어있다.
app.use(cookieParser(process.env.COOKIE_SECRET));

app.use(
  session({
    resave: false, //요청이 올때 세션에 수정사항이 생기지 않더라도 세션을 다시 저장할지 설정
    saveUninitialized: false, //세션에 저장할 내역이 없더라도 처음부터 세션을 생성할지 설정하는 것
    secret: process.env.COOKIE_SECRET, //세션관리시 클라이언트에 쿠키를 보냄 안전하게 쿠키를 전송하려면 서명을 추가
    cookie: {
      //클라이언트에서 쿠리를 확인하지 못하도록 설정
      httpOnly: true,
      //https가 아닌환경에서도 사용할수 있도록 ( 배포시에는 true를 설정하고 https 를 적용하는것이 좋다)
      secure: false,
    },
    name: 'session-cookie',
  })
);

//app.use에 매개변수가 req,res,next 인 함수를 넣으면 된다.
//미들웨어는 위에서 아래로 순서대로 실행되면서 요청과 응답 사이에 특별한 기능을 추가 할수 있다.
//next라는 세번째 매개변수는 다음 미들웨어로 넘어가는 함수이다. 실행하지않으면 다음 미들웨어가 실행되지않음
app.use((req, res, next) => {
  console.log('모든 요청에 다 실행됩니다.');
  next();
});

//app.get(주소,라우터)는 주소에 대한 GET요청이 올때 어떤 동작을 할지 작성할수있다.
//app.get의 두번째 미들웨어에서 에러가 발생하고 아래 에러 처리 미들웨어로 전달
app.get(
  '/',
  (req, res, next) => {
    console.log('GET / 요청에서만 실행됩니다.');
    next();
  },
  (req, res) => {
    throw new Error('에러는 에러 처리 미들웨어로 갑니다');
  }
);

//에러처리 미들웨어는 매개변수를 사용하지않더라도 네개를 가져야한다
app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).send(err.message);
});

app.listen(app.get('port'), () => {
  //app.set()을 이용하여 저장한 값을 불러올수있다.
  console.log(app.get('port'), ' server run');
});
