'use strict';

const allBtns = document.querySelectorAll('.theme-button');

allBtns.forEach(btn => {
	btn.addEventListener('click', () => {
		const theme = btn.getAttribute('data-theme-name');
		document.documentElement.setAttribute('data-theme', theme);
		document.cookie = `theme=${theme}; path=/; max-age=${60*60*24*365}`;
	});
});
