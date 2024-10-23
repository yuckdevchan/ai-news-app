document.addEventListener("DOMContentLoaded", updateWeather); // Update weather on page load
setInterval(updateWeather, 600000); // Update weather every 10 minutes

document.addEventListener("DOMContentLoaded", updateTime); // Update time on page load
setInterval(updateTime, 1000); // Update time every second