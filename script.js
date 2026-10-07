const BACKEND_URL = "http://127.0.0.1:8000"; 

async function checkURL() {
  const url = document.getElementById("urlInput").value;
  const resultElement = document.getElementById("result");

  if (!url) {
    alert("Please enter a URL");
    return;
  }

  resultElement.innerHTML = "Checking...";
  resultElement.className = "badge"; 

  try {
    const response = await fetch(`${BACKEND_URL}/check_url/?url=${encodeURIComponent(url)}`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();

  
    setTimeout(() => {
      resultElement.innerHTML = `Risk Level: <strong>${data.risk_level}</strong>`;

      if (data.risk_level === "Safe") {
        resultElement.classList.add("safe");
      } else if (data.risk_level === "Suspicious") {
        resultElement.classList.add("suspicious");
      } else {
        resultElement.classList.add("dangerous");
      }
    }, 4000);
  } catch (error) {
    console.error("Error:", error);
    resultElement.innerHTML = "Error fetching data.";
    resultElement.className = "badge dangerous";
  }
}
document.getElementById("checkButton").addEventListener("click", checkURL);
