const ctx = document.getElementById('languageChart');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: Object.keys(languageCounts),
    datasets: [{
      label: 'Repos per Language',
      data: Object.values(languageCounts),
      backgroundColor: '#1DB954'
    }]
  }
});