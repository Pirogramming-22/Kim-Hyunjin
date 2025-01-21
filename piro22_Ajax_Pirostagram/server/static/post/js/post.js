//console.log('정상적용');
const like_btn = document.querySelectorAll('.heartButton');

like_btn.forEach((btn) => {
    btn.addEventListener('click', async (e) => {
        const target = e.target;
        const pk = target.getAttribute('data-pk');
        const url = "/like/";
         const { data } = await axios.post(url, {
                pk
            });
         //console.log(data);


            const { id, like, clicked } = data;

            const likeHandleResponse = (id, like, clicked) => {
                const element = document.querySelector(`.post-${id} .heart-icon > path`);
                if (clicked == true) {  // true/false boolean check
                    element.setAttribute('fill', 'red');
                    element.setAttribute('stroke', 'red');
                } else {
                    element.setAttribute('fill', 'black');
                    element.setAttribute('stroke', 'white');
                }
                const text = document.querySelectorAll('.like-num')
                if(like>1){
                    text[id-1].innerText = `Pirogramming 님외 ${like - 1}명이 좋아합니다.`;
                }else if(like==1){
                    text[id-1].innerText = 'Pirogramming 님이 좋아합니다.';
                }else{
                    text[id-1].innerText = '';
                }
            };

            likeHandleResponse(id, like, clicked);
    });
});
