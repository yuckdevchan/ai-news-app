function updateTime() {
    const timeText = document.getElementById('timeText');
    const date = new Date();
    timeText.innerText = date.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });
}