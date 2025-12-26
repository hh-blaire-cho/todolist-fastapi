# todolistapp-fastapi

## 사용 기술
- FastAPI
- PostGreSQL

## 프론트에 붙여보기:
서버를 띄운 후 [여기](https://www.todobackend.com/client/index.html?http://localhost:8000/todos) 를 클릭하여, UI를 동작해보세요
`https://www.todobackend.com/` 에서 준비된 프론트입니다.

## 스펙 확인 하기:
서버를 띄운 후 [여기](https://www.todobackend.com/specs/index.html?http://localhost:8000) 를 클릭해서 pass/fail을 확인해보세요. </br>
- 또는 [여기](https://www.todobackend.com/specs/index.html)에 접속한 뒤 `http://localhost:8000/` 를 복사 붙여넣기기 해 넣고 돌려보세요.</br>
- 브라우저 보안모드가 아니라면 아래 에러가 뜰 수 있으며 이는 백앤드잘못이 아닙니다.
  ```angular2html 
     the api root responds to a GET (i.e. the server is up and accessible, CORS headers are set up) 
     Error: global leaks detected: crosswebex_nativecall, touchenex_nativecall 
      at Runner.checkGlobals (https://www.todobackend.com/specs/js/lib/mocha.js:4532:21) 
      at Runner.<anonymous> (https://www.todobackend.com/specs/js/lib/mocha.js:4408:44)at EventEmitter.emit (https://www.todobackend.com/specs/js/lib/mocha.js:588:20) 
      at https://www.todobackend.com/specs/js/lib/mocha.js:4817:14 
      at done (https://www.todobackend.com/specs/js/lib/mocha.js:4300:5) 
      at https://www.todobackend.com/specs/js/lib/mocha.js:4341:31 
      at _fulfilled (https://www.todobackend.com/specs/js/lib/q.js:787:54) 
      at https://www.todobackend.com/specs/js/lib/q.js:816:30 
      at Promise.promise.promiseDispatch (https://www.todobackend.com/specs/js/lib/q.js:749:13) 
      at https://www.todobackend.com/specs/js/lib/q.js:557:44
  ```


## API 문서 확인 하기:
서버를 띄운 후 아래로 로 접속 </br>
-  [Swagger UI](http://localhost:8000/docs) 인터랙티브 문서(try it out 가능)!!
-  [ReDoc](http://localhost:8000/redoc) 깔끔한 정적 문서 스타일
