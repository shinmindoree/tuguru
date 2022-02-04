
// html tag통해서 해당하는 변수를 저장한다
const ticker = document.querySelector("td#ticker");


// table 안의 ticker를 변수로 추출한다
const TICKER = ticker.innerText;


// 이 변수를 input으로 받아서 API Call날리는 함수를 작성 후, 이를 html에 표시한다

function getPrice(TICKER) {

}

// 함수 바로 실행하고 이루 5초마다 숫자 업데이트 한다
getPrice();
setInterval(getPrice, 5000);