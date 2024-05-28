document.addEventListener('DOMContentLoaded', postData)

const data = document.location.search;
const params = new URLSearchParams(data);

const name = params.get('fname');
const amount = params.get('amount');
const genres = params.get('genres');
const movie = params.get('movie');
const thriller = params.get('thriller');
const sweets = params.get('sweets');

let characters;

if (amount >= 7) { //and&&, or||, in, not!
    characters = 'very addicted to walnut brownies!!';
    image = 'images/walnut brownie.jpeg';
} else if (sweets == "mint" || genres == "horror"){
    characters = 'so weird... You can have a peppermint brownie...'
    image = 'images/peppermint brownies.jpeg';
} else if (sweets == "mnm" || thriller == "rainy"){
    characters = 'too cute! Take my m&ms!'
    image = 'images/m&m brownies.jpeg';
} else if (sweets == "caramel" || thriller == "cloudy" || genres == "drama"){
    characters = 'being gooey like a caramel brownie!'
    image = 'images/caramel brownie.jpeg';
} else if (sweets == "starburst" || thriller == "sunny" || genres == "action"){
    characters = 'special like cookies and cream!'
    image = 'images/cookies and cream.jpeg';
} else {
    characters = 'soooooo classic!'
    image = 'images/classic brownie.jpeg';
}

//writing html code

function postData() {
    const container = document.getElementById('results');
    container.innerHTML = `<h1>You are ${characters}</h1>
                            <img src="${image}"></img>`;
}


