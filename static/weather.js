function updateWeather() {
    // get location from browser and then get weather from open meteo
    navigator.geolocation.getCurrentPosition((position) => {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      var response = fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m`);
      response.then((response) => {
        response.json().then((data) => {
          console.log(data)
          const temp = data.current.temperature_2m;
          document.getElementById("weatherText").innerText = `${temp}°C`;
        });
      });
    });
  }