const form = document.getElementById('input-form');
form.addEventListener('submit', async (event) => {
  // Prevent the form from submitting normally
  event.preventDefault();

  // Get the input value from the form
  const input = document.getElementById('input-text').value;
  print(input)

  // Send a POST request to the FastAPI backend
  const response = await fetch('/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ input: input })
  });

  // Get the response data and update the HTML
  const data = await response.json();
  const responseArea = document.getElementById('response-area');
  responseArea.innerHTML = `<h5>${data.output}</h5>`;
});
