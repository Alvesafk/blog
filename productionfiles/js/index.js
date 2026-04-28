'use strict';

const aboutLink = document.getElementById("about-link");
const postsLink = document.getElementById("posts-link");

function setupEventListeners() {
	if(aboutLink) {
		aboutLink.classList.add("is-disabled");
	}
}

document.addEventListener('DOMContentLoaded', setupEventListeners);
