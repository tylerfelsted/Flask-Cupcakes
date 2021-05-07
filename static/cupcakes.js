API_BASE_URL = 'http://localhost:5000/api';
$cupcakeContainer = $('#cupcake-container');
$newCupcakeButton = $('#new-cupcake')
$flavorInput = $('#flavor')
$sizeInput = $('#size')
$ratingInput = $('#rating')
$imageInput = $('#image')

getCupcakes()

$newCupcakeButton.click(addCupcake)


async function getCupcakes() {
    const resp = await axios.get(`${API_BASE_URL}/cupcakes`);
    const data = resp.data.cupcakes;
    for(let i = 0; i < data.length; i++) {
        appendNewCupcake(data[i]);
    }
}



async function addCupcake(e) {
    e.preventDefault();
    const data = {
        flavor: $flavorInput.val(),
        size: $sizeInput.val(),
        rating: $ratingInput.val(),
        image: $imageInput.val()
    };
    
    const resp = await axios.post(`${API_BASE_URL}/cupcakes`, data);
    appendNewCupcake(resp.data.cupcake)
}


function appendNewCupcake(cupcake) {
    $cupcakeContainer.append(`
    <div class="col">
        <div class="card" style="width: 18rem;">
            <img src="${cupcake.image}" class="card-img-top" alt="">
            <div class="card-body">
                <h5 class="card-title">${cupcake.flavor}</h5>
                <p class="card-text">Size: ${cupcake.size}</p>
                <p class="card-text">Rating: ${cupcake.rating}</p>
            </div>
        </div>
    </div>
    `);
}