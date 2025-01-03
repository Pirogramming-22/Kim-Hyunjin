let screen = document.querySelector('.screen');
const start_button = document.querySelector('#start-button');
const stop_button = document.querySelector('#stop-button');
const reset_button = document.querySelector('#reset-button');
const round_button = document.querySelector(".round-btn");
const record_sheet = document.querySelector('.record-sheet');
const all_check = document.querySelector('#all-checked');
const remover = document.querySelector('.delete-button');
const record_control = document.querySelector('.record-sheet-control');


let start;
let end;
let history;
let running_flag;
let timer;
let button_arr;

function start_stop_watch(){
  start_button.setAttribute('disabled', "true");
  if(!running_flag){
    start = Date.now();
    running_flag = true;
    timer = setInterval(() => {
      end = Date.now();
      const time_gap = end - start;
      //console.log(time_gap)
      const sec = Math.floor(time_gap / 1000);
      const msec = Math.floor((time_gap % 1000) / 10);  // 밀리초의 두 자리로 출력
      screen.innerText = `${sec}:${msec.toString().padStart(2, '0')}`;}, 10);
  }else{
    //console.log("--------------------------");
    stop_button.removeAttribute('disabled', "true");
    start = Date.now();
    timer = setInterval(() => {
      end = Date.now();
      const time_gap = end - start + history;
     // console.log(time_gap);
      const sec = Math.floor(time_gap / 1000);
      const msec = Math.floor((time_gap % 1000) / 10);  // 밀리초의 두 자리로 출력
      screen.innerText = `${sec}:${msec.toString().padStart(2, '0')}`;}, 10);
  }
  }

function stop_stop_watch(){
  if(running_flag){
    stop_button.setAttribute('disabled', "true");
    history += (end - start)
    start_button.removeAttribute('disabled', "true");
    clearInterval(timer);
    add_record();
  }
}

//reset이랑 delete 수정

function reset_stop_watch(){
  start = 0;
  end = 0;
  history = 0;
  screen.innerText = '00:00';
  running_flag = false;
  clearInterval(timer);
  localStorage.setItem('saved_time', 0);
}

function isAllChecked(list){
  for(let i=1; i<list.length; i++){
    if(list[i].children[0].children[0].classList.contains('hidden')){
      return false;
    }
  }
  return true;
}


function add_record(){
  const container = document.createElement("div");
  
  const btn = document.createElement("button");
  btn.className = "round-btn";

  const p = document.createElement("p");
  p.classList.add("hidden", "check-sign");

  const p2 = document.createElement("p");
  p2.innerText = screen.innerText;
  p2.id = "detail";
  p.innerText = "✔️";

  btn.appendChild(p);
  btn.addEventListener("click", () => {
    p.classList.toggle("hidden");
    p.classList.toggle("checked");
    if(isAllChecked(button_arr)){
      button_arr[0].children[0].children[0].classList.remove('hidden');
      button_arr[0].children[0].children[0].classList.add('checked');
    }else{
      button_arr[0].children[0].children[0].classList.add('hidden');
      button_arr[0].children[0].children[0].classList.remove('checked');
    }
  })
  container.append(btn, p2);
  container.className = "record-content";
  record_sheet.appendChild(container);
  button_arr.push(container);
}

all_check.addEventListener("click", (event) => {
  if(!isAllChecked(button_arr)){
    for(let i=0; i<button_arr.length; i++){
      if(button_arr[i].children[0].children[0].classList.contains('hidden')){
        button_arr[i].children[0].children[0].classList.remove('hidden');
        button_arr[i].children[0].children[0].classList.add('checked');
      }
    }
  }else{
    for(let i=0; i<button_arr.length; i++){
        button_arr[i].children[0].children[0].classList.add('hidden');
        button_arr[i].children[0].children[0].classList.remove('checked');
    }
  }
});

start_button.addEventListener("click", start_stop_watch);
stop_button.addEventListener("click", stop_stop_watch);
reset_button.addEventListener("click", reset_stop_watch);

remover.addEventListener("click", () => {
  // 첫 번째 버튼 상태 확인 및 처리
  const firstButton = button_arr[0]?.children[0]?.children[0];
  if (firstButton && !firstButton.classList.contains('hidden')) {
    firstButton.classList.add('hidden');
    firstButton.classList.remove('checked');

    // 두 번째 이후 버튼들 제거
    for (let i = button_arr.length - 1; i > 0; i--) {
      const element = button_arr[i];
      element.remove(); // DOM에서 제거
      button_arr.splice(i, 1); // 배열에서 제거
      localStorage.setItem('saved_time', history);
      location.reload();
    }
  } else {
    // 체크된 버튼만 제거
    for (let i = button_arr.length - 1; i > 0; i--) {
      const element = button_arr[i];
      const child = element.children[0]?.children[0];
      if (child && child.classList.contains('checked')) {
        element.remove(); // DOM에서 제거
        button_arr.splice(i, 1); // 배열에서 제거
      }
    }
  }
});

document.addEventListener("DOMContentLoaded", () => {
  if(localStorage.getItem('saved_time') != 0){
    start = 0;
    end = 0;
    history = parseInt(localStorage.getItem('saved_time'));
    running_flag = true;
    button_arr =[record_control];
      //console.log(time_gap);
    const sec = Math.floor(history/ 1000);
    const msec = Math.floor((history % 1000) / 10);  // 밀리초의 두 자리로 출력
    screen.innerText = `${sec}:${msec.toString().padStart(2, '0')}`;
  }else{
    start = 0;
    end = 0;
    history = 0;
    running_flag = false;
    timer;
    button_arr =[record_control];
  }
  
});
