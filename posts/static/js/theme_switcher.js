'use strict';

const allBtns = document.querySelectorAll('.theme-button');

function disableSelected() {
	allBtns.forEach(btn => {
		const actualTheme = document.documentElement.getAttribute('data-theme');
		const btnTheme = btn.getAttribute('data-theme-name');
		if (btnTheme === actualTheme) btn.classList.add('is_disabled_btn'); else btn.classList.remove('is_disabled_btn');
	});
}

allBtns.forEach(btn => {
	btn.addEventListener('click', () => {
		const theme = btn.getAttribute('data-theme-name');
		document.documentElement.setAttribute('data-theme', theme);
		document.cookie = `theme=${theme}; path=/; max-age=${60*60*24*365}`;
		disableSelected();
	});
});

disableSelected();
