fetch('http://127.0.0.1:8081/api/posts')
  .then(function(response) {
    return response.json()
  })
  .then(function(data) {
    console.log(data)
    renderPosts(data)
  })

function renderPosts(data) {
  let postHtml = ''

  for (i = 0; i < data.length; i++) {
    postHtml += `
      <div class="card">
        <a href="#">
          <img src="https://fakeimg.pl/250x150/" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">
              ${ data[i].title }
            </h5>
            <p class="card-text">
              ${ data[i].content }
            </p>
          </div>
        </a>
      </div>
    `
  }
  
  let postGroupHtml = `
    <div class="card-columns">
      ${postHtml}
    </div>
  `

  $('.container').append(postGroupHtml)
}