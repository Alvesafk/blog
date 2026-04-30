'use strict';

const btn = document.getElementById('theme-icon-div');
let currentTheme = document.documentElement.getAttribute("data-theme");

function changeThemeIcon() {
	currentTheme = document.documentElement.getAttribute("data-theme");

	const isDark = currentTheme === "dark";
	const iconAdd = isDark ? "fa-moon" : "fa-sun";
	const iconRemove = !isDark ? "fa-moon" : "fa-sun";

	const themeIcon = document.getElementById("theme-icon");

	themeIcon.classList.add(iconAdd);
	themeIcon.classList.remove(iconRemove);
}

btn.addEventListener("click", function() {
    let theme = document.documentElement.getAttribute("data-theme");
    let targetTheme = (theme === "dark") ? "light" : "dark";

    document.documentElement.setAttribute("data-theme", targetTheme);
    
    document.cookie = `theme=${targetTheme}; path=/; max-age=${60*60*24*365}`;

	changeThemeIcon();
});

changeThemeIcon();
