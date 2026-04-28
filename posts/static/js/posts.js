'use strict';

const container = document.getElementById('container-posts');
const postsLink = document.getElementById('posts-link');

function setupEventListeners() {
	if (container) {
        container.addEventListener('click', (event) => {
            const card = event.target.closest('.clickable-post');

            if (card) {
                const url = card.dataset.url;
                
                window.location.href = url;
            }
        });
    }

	if (postsLink) {
		postsLink.classList.add("is-disabled");
	}
}

document.addEventListener('DOMContentLoaded', setupEventListeners);
