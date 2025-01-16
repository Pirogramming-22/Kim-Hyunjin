
document.addEventListener('DOMContentLoaded', function () {
    const fourcont = document.querySelector("#four-content-container");
    const idea_list = document.querySelectorAll(".idea-content-container");
    const favoriteBtn = document.querySelectorAll('.favorite-button');
    const pbtn = document.querySelectorAll('.plus-btn');
    const mbtn = document.querySelectorAll('.minus-btn');
    //const sorting = document.querySelector('#sorting');

    // DOM이 로드된 후 실행할 코드

    //console.log(sorting.value)

    for (let i = 0; i < favoriteBtn.length; i++) {
        check_starred(favoriteBtn[i], i + 1);
    }

    switch (idea_list.length) {
        case 1:
            fourcont.className = '';
            fourcont.classList.add('four-content-container-base');
            break;
        case 2:
            fourcont.className = '';
            fourcont.classList.add('four-content-container-two');
            break;
        case 3:
            fourcont.className = '';
            fourcont.classList.add('four-content-container-three');
            break;
        case 4:
            fourcont.className = '';
            fourcont.classList.add('four-content-container-four');
            break;
        default:
            fourcont.className = '';
            fourcont.classList.add('four-content-container-four');
            break;
    }

    favoriteBtn.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            let target = e.target;
            const parents = [];
            while (target.parentElement) {
                target = target.parentElement;
                parents.push(target);
            }

            // 아이템의 ID를 추출
            const key = parents[2].querySelector('h3 > a').href.split('/').pop();

            const isFavorite = parents[1].getAttribute('data-favorite') === 'true';
            //console.log(isFavorite)
            parents[1].setAttribute('data-favorite', !isFavorite);
            const svg = parents[1].querySelector('svg');
            svg.style.fill = !isFavorite ? 'yellow' : 'transparent';

            fetch(`ideas/change/${key}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                .then(response => response.json())
                .catch(error => {
                    console.error('Fetch error:', error);
                });
        });
    });

    function check_starred(obj, key) {
        const isFavorite = obj.getAttribute('data-favorite') === 'true';
        const newFavoriteState = !isFavorite;

        fetch(`ideas/check/${key}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.starred) {
                    obj.setAttribute('data-favorite', newFavoriteState);
                    const svg = obj.querySelector('svg');
                    svg.style.fill = 'yellow';
                } else {
                    obj.setAttribute('data-favorite', isFavorite);
                    const svg = obj.querySelector('svg');
                    svg.style.fill = 'transparent';
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
            });
    }

     pbtn.forEach((btn) => {
        btn.addEventListener('click', (e) => {
             let target = e.target;
        const parents = [];
        while (target.parentElement) {
            target = target.parentElement;
            parents.push(target);
        }
        const key = parents[2].querySelector('h3 > a').href.split('/').pop();
        //console.log(key)
        fetch(`ideas/add/${key}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
            .then(response => response.json())
            .then(
                data => {
                    parents[1].querySelector('p > span').innerText = data.interest;
                })
            .catch(error => {
                console.error('Fetch error:', error);
            });
        });
    });


    mbtn.forEach((btn) => {
        btn.addEventListener('click', (e) => {
             let target = e.target;
        const parents = [];
        while (target.parentElement) {
            target = target.parentElement;
            parents.push(target);
        }
        const key = parents[2].querySelector('h3 > a').href.split('/').pop();
        //console.log(parents[1].querySelector('p > span'));
        //console.log(key)
        fetch(`ideas/minus/${key}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        })
            .then(response => response.json())
            .then(data => {
                parents[1].querySelector('p > span').innerText = data.interest;
            })
            .catch(error => {
                console.error('Fetch error:', error);
            });
        });
    });

    /*sorting.addEventListener('change', function () {

    })*/
});