/*input 0~9
시도 가능 횟수 9번
숫자와 위치가 전부 틀리면 아웃이 되고 O 로 출력합니다.
**아웃**이 아닌 경우 [ (스트라이크 카운트) **S** (볼 카운트) **B** ] 형태로 출력됩니다.
    - 숫자는 맞지만 위치가 틀리면 **볼** 카운트가 **1 증가**합니다.
    - 숫자와 위치가 전부 맞으면 **스트라이크** 카운트가 **1 증가**합니다.
모든 숫자가 맞은 경우 (= S 카운트가 3인 경우) 게임에서 승리하며 승리 이미지를 출력합니다.
9번의 기회 안에 모든 숫자를 찾지 못했을 경우 게임에서 패배하며 패배 이미지를 출력합니다.
answer---중복되지 않는 3개의 랜덤한 숫자를 설정합니다.
html의 input과 결과창의 내용을 비운다.
*/

const number1 = document.querySelector("#number1"); //첫번재 숫자
const number2 = document.querySelector("#number2"); //두번재 숫자
const number3 = document.querySelector("#number3"); //세번재 숫자

const gameResult = document.querySelector("#game-result-img"); //게임 최종 결과창
const attempts = document.querySelector("#attempts"); //게임 시도 잔여 횟수
const result = document.querySelector("#results"); //게임 결과창
const remainingAttempts = document.querySelector(".remaining-attempts");
const btn = document.querySelector(".submit-button");//button

let answer=[];//정해진 정답
let attempt = 9;

function game_set(){
  let completed = true;
  
  while (completed) {
    let created_num = Math.floor(Math.random() * 10);

    if (!answer.includes(created_num)) {
        answer.push(created_num);
    }

    if (answer.length === 3) {
        completed = false;
    }
  }
  console.log(answer);
  attempts.innerHTML = `${attempt.toString()}`;
};

function add_div(results) {
  result.style.width = 100+"%";

  const newResult = document.createElement("div");
  const leftInput = document.createElement("div");
  const rightInput = document.createElement("div");
  const strikeIcon = document.createElement("div");
  const ballIcon = document.createElement("div");
  const outIcon = document.createElement("div");

  rightInput.className = "right";
  leftInput.className = "left";
  leftInput.innerText = `${number1.value} ${number2.value} ${number3.value}`;
  //console.log(leftInput);
  if (results[5] >= 3) {
      outIcon.classList.add("num-result", "out");
      outIcon.innerText = "O";
      rightInput.appendChild(outIcon);
      newResult.append(leftInput, ' :', rightInput);
      newResult.className = "check-result";
      result.appendChild(newResult);
      attempt -= 1;
      if (attempt === 0) {
          remainingAttempts.style.display = "none";
          gameResult.src = "./fail.png";
          btn.disabled = true;
      }
  } else if (results[3] < 3) {
      strikeIcon.classList.add("num-result", "strike");
      strikeIcon.innerText = "S";
      ballIcon.classList.add("num-result", "ball");
      ballIcon.innerText = "B";
      rightInput.append(`${results[3]} `, strikeIcon, ` ${results[4]} `, ballIcon);
      newResult.append(leftInput, ':', rightInput);
      newResult.className = "check-result";
      result.appendChild(newResult);
      attempt -= 1;
      if (attempt === 0) {
          remainingAttempts.style.display = "none";
          gameResult.src = "./fail.png";
          btn.disabled = true;
      }
  } else {
      strikeIcon.classList.add("num-result", "strike");
      strikeIcon.innerText = "S";
      ballIcon.classList.add("num-result", "ball");
      ballIcon.innerText = "B";
      rightInput.append(`${results[3]} `, strikeIcon, ` ${results[4]} `, ballIcon);
      newResult.append(leftInput, ':', rightInput);
      newResult.className = "check-result";
      result.appendChild(newResult);
      attempt -= 1;
      remainingAttempts.style.display = "none";
      gameResult.src = "./success.png";
      btn.disabled = true;
  }
};


function check_numbers(event){
  //console.log(number1.value);
  //console.log(number2.value);
  //console.log(number3.value);
  if(number1.value===""||number2.value===""||number3.value===""){
    number1.value="";
    number2.value="";
    number3.value="";
    return
  }// 빈칸 입력시 input 삭제
  if (/[^0-9.]/.test(number1.value) || /[^0-9.]/.test(number2.value) || /[^0-9.]/.test(number3.value))
  {
    number1.value="";
    number2.value="";
    number3.value="";
    return
  } // 숫자 이외 데이터 입력시 input 삭제

  const results = [];

  for(let i =0; i<3; i++){
    if (i===0 && answer[i] === parseInt(number1.value)){
      results.push('strike');
    }else if (i===1 && answer[i] === parseInt(number2.value)){
      results.push('strike');
    }else if (i===2 && answer[i]=== parseInt(number3.value)){
      results.push('strike');
    }else if(i===0 && (answer[i] === parseInt(number2.value)||answer[i]=== parseInt(number3.value))){
      results.push('ball');
    }else if(i===1 && (answer[i] === parseInt(number1.value)||answer[i]=== parseInt(number3.value))){
      results.push('ball');
    }else if(i===2 && (answer[i] === parseInt(number1.value)||answer[i]=== parseInt(number2.value))){
      results.push('ball');
    }else{
      results.push('out');
    }
  }
  //결과 arr 저장
  results.push(results.filter(item => item === "strike").length);
  results.push(results.filter(item => item === "ball").length);
  results.push(results.filter(item => item === "out").length);
  //결과 개수 counting
  add_div(results);
  attempts.innerHTML = `${attempt.toString()}`;
  number1.value="";
  number2.value="";
  number3.value="";
  };

game_set();