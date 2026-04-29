'use strict';

const timeStat = document.getElementById('time-stat');

const observer = new PerformanceObserver((list) => {
	const entries = list.getEntries();
	
	const lastEntry = entries[entries.length - 1];
	const totalTime = (lastEntry.loadEventEnd - lastEntry.startTime) / 1000;
	const formattedTime = totalTime.toFixed(2);

	timeStat.textContent = `The page was loaded in ${formattedTime} seconds!`;
});

observer.observe({ type: 'navigation', buffered: true });
