'use strict';

const aboutLink = document.getElementById("about-link");
const postsLink = document.getElementById("posts-link");
const post = document.getElementById("recent-post");

function setupEventListeners() {
	if(aboutLink) {
		aboutLink.classList.add("is-disabled");
	}

	if(post) {
		post.addEventListener('click', () => {
			const postId = post.getAttribute('data-id');
			window.location.href = `/posts/${postId}`;
		});
	}
}

document.addEventListener('DOMContentLoaded', setupEventListeners);
