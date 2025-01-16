
document.addEventListener('DOMContentLoaded', function () {
    const favoriteBtn = document.querySelector('.favorite-button');

    // DOM이 로드된 후 실행할 코드

    check_starred(favoriteBtn, parseInt(window.location.href.split('/').pop()));

     favoriteBtn.addEventListener('click', (e) => {
        let target = e.target;
        const parents = [];
        while (target.parentElement) {
            target = target.parentElement;
            parents.push(target);
        }
        const key = window.location.href.split('/').pop();
        //console.log(urlarr);
        //console.log(parents)
        const isFavorite = parents[1].getAttribute('data-favorite') === 'true';
        //console.log(isFavorite)
        parents[1].setAttribute('data-favorite', !isFavorite);
        const svg = parents[1].querySelector('svg');
        svg.style.fill = !isFavorite ? 'yellow' : 'transparent';



        fetch(window.location.origin.concat(`/ideas/change/${key}`), {
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

function check_starred(obj, key) {
    const isFavorite = obj.getAttribute('data-favorite') === 'true';
    const newFavoriteState = !isFavorite;

    fetch(window.location.origin.concat(`/ideas/check/${key}`), {
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
});