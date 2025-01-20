//console.log('정상적용');
const like_btn = document.querySelectorAll('.heartButton');

like_btn.forEach((btn) => {
    btn.addEventListener('click', async (e) => {
        const target = e.target;
        const pk = target.getAttribute('data-pk');
        const url = "like/";
         const { data } = await axios.post(url, {
                pk
            });
         //console.log(data);


            const { id, like, clicked } = data;
            //console.log(data);

            const likeHandleResponse = (id, like, clicked) => {
                const element = document.querySelector(`.comment-${id} .heart-icon > path`);
                if (clicked == true) {  // true/false boolean check
                    element.setAttribute('fill', 'red');
                    element.setAttribute('stroke', 'red');
                } else {
                    element.setAttribute('fill', 'transparent');
                    element.setAttribute('stroke', 'white');
                }
                const text = document.querySelector(`.like-num-${id}`);
                //console.log(`.like-num-${id}`);
                if(like>0){
                    text.innerText = `${like}`;
                }else{
                    text.innerText = '';
                }
            };

            likeHandleResponse(id, like, clicked);
    });
});

async function submitComment() {
    const commentInput = document.getElementById('comment-input');
    const text = commentInput.value.trim();
    const postId = commentInput.getAttribute('data-pk');

    if (!text) {
        alert('댓글을 입력하세요.');
        return;
    }

    const response = await fetch('/create-comment/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // CSRF 토큰 추가
        },
        body: JSON.stringify({ post_id: postId, text: text })
    });

    const data = await response.json();

    if (response.ok) {
        location.reload(true);
        commentInput.value = '';
    } else {
        alert(`댓글 등록 실패: ${data.error}`);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}