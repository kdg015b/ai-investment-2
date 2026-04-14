document.addEventListener('DOMContentLoaded', function() {
    // Load and display the crypto portfolio
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('portfolio-container');
            if (!data || data.length === 0) {
                container.innerHTML = '<p>No portfolio data available.</p>';
                return;
            }

            let html = '<ul>';
            data.forEach(asset => {
                html += `<li><b>${asset.asset} (${asset.ticker})</b>: ${asset.weight}%`;
                if (asset.price) {
                    html += ` - Price: $${asset.price.toFixed(2)}`;
                }
                html += '</li>';
            });
            html += '</ul>';
            container.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching crypto portfolio data:', error);
            const container = document.getElementById('portfolio-container');
            container.innerHTML = '<p>Could not load crypto portfolio data.</p>';
        });

    // Load and display the Korean stock portfolio
    fetch('/api/korean_stocks')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('korean-stock-container');
            if (!data || data.length === 0) {
                container.innerHTML = '<p>No Korean stock data available.</p>';
                return;
            }

            let html = '<ul>';
            data.forEach(stock => {
                html += `<li>
                    <h4>${stock.name} (${stock.ticker})</h4>
                    <p><b>선정 이유:</b> ${stock.reason}</p>
                    <p><b>투자 전략:</b> ${stock.strategy}</p>
                </li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching Korean stock data:', error);
            const container = document.getElementById('korean-stock-container');
            container.innerHTML = '<p>Could not load Korean stock data.</p>';
        });

    // Load and display the news articles
    fetch('news.json?t=' + new Date().getTime())
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('news-container');
            if (!data || data.length === 0) {
                container.innerHTML = '<p>No news articles available.</p>';
                return;
            }

            let html = '<ul>';
            data.forEach(article => {
                html += `<li>
                    <h4><a href="${article.url}" target="_blank">${article.title}</a></h4>
                    <p>${article.description || 'No description available.'}</p>
                </li>`;
            });
            html += '</ul>';
            container.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching news data:', error);
            const container = document.getElementById('news-container');
            container.innerHTML = '<p>Could not load news data.</p>';
        });
});
